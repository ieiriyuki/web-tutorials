import asyncio
from random import randint
from typing import Optional
import redis
from fastapi import FastAPI
from pydantic import BaseModel
from repository import CreditRepository
app = FastAPI()
global_items = {}


class Credit(BaseModel):
    id: int
    amount: int


class CreditResult(BaseModel):
    id: int
    result: str
    current_credit: Optional[int] = None
    total_credit: int


def make_redis_client(host: str="redis", port: int=6379, db: int=0):
    return redis.Redis(host=host, port=port, db=db, decode_responses=True)


@app.on_event("startup")
def startup_event():
    reader = make_redis_client(db=0)
    writer = make_redis_client(db=1)
    credit_repository = CreditRepository(reader, writer)
    credit_repository.initialize_credit()
    global_items["credit_repository"] = credit_repository


@app.post("/")
async def make_credit(credit: Credit):
    threshold = 2000

    current_credit = global_items["credit_repository"].get_credit(credit.id)
    await asyncio.sleep(randint(0, 10))

    if current_credit is None:
        return CreditResult(
            id=credit.id,
            result="NG",
            current_credit=current_credit,
            total_credit=0,
        )

    total_credit = current_credit + credit.amount

    if total_credit > threshold:
        return CreditResult(
            id=credit.id,
            result="NG",
            current_credit=current_credit,
            total_credit=total_credit,
        )
    else:
        global_items["credit_repository"].add_credit(credit.id, credit.amount)
        return CreditResult(
            id=credit.id,
            result="OK",
            current_credit=current_credit,
            total_credit=total_credit,
        )
