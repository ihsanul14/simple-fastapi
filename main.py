from fastapi import FastAPI
import uvicorn
from decouple import config
from framework.delivery import HttpDelivery

app = FastAPI()
HttpDelivery(app).delivery_http()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=int(config('PORT')))