# payment-service/app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/payment")
def read_payment():
    return {
        "payment_id": 100,
        "order_id": 1,
        "status": "Success",
        "amount": 499
    }
