from pydantic import BaseModel

class SpamRequest(BaseModel):
    message: str
