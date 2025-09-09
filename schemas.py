from pydantic import BaseModel

class URLStr(BaseModel):
    url: str