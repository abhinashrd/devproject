# order-service/app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/order")
def read_order():
    return {
        "order_id": 1,
        "item": "Book",
        "quantity": 2,
        "price": 499
    }
