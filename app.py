import os
from schemas import URLStr
from preprocess import Preprocessor
from models import Model
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse


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

@app.get("/")
def serve_home():
    return FileResponse(os.path.join("static", "index.html"))

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
    

