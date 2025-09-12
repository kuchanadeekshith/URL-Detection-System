import os
from schemas import URLStr
from preprocess import Preprocessor
from models import Model
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse

def ResultCategories(result):
    result=int(result)
    if result==0:
        return {result:"defacement"}
    elif result==1:
        return {result:"malware"}
    else:
        return {result:"phishing"}

app=FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def serve_home():
    file_path = os.path.join(os.getcwd(), "static", "index.html")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>URL Detection System is running!</h1>"

@app.head("/")
def health_check():
    return {}

@app.on_event("startup")
def load_models():
    global binary_model, multi_model
    binary_model = Model.load_binary()
    multi_model = Model.load_multi()


@app.post("/prediction")
def prediction(url: URLStr)-> dict:
    processed_url=Preprocessor.preprocess(url.url)
    result=binary_model.predict(processed_url)

    if result[0].item()==0:
        return {"result":'Safe'}
    else:
        result=multi_model.predict(processed_url)
        return ResultCategories(result[0].item())
    

