from fastapi import Body, FastAPI
from pydantic import BaseModel
import time

from app.model.model import generate_like_terms

app = FastAPI()


class TextIn(BaseModel):
    text: str


class TokensOut(BaseModel):
    tokens: list[str]


@app.get('/')
def home():
    return {"health_check": "OK"}


@app.post('/tokenize')
def tokenize(payload: dict = Body(...)):
    time.sleep(0.1)

    tokens = generate_like_terms(payload['query'])
    return tokens
