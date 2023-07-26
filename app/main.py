from fastapi import Body, FastAPI
from pydantic import BaseModel
import time

from app.model.model import createTokens

app = FastAPI()


class TextIn(BaseModel):
    text: str


class TokensOut(BaseModel):
    tokens: object


@app.get('/')
def home():
    return {"health_check": "OK"}


@app.post('/tokenize')
def tokenize(payload: dict = Body(...)):
    time.sleep(0.3)

    tokens = createTokens(payload['query'])
    return tokens
