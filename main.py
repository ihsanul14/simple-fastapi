from fastapi import FastAPI
import delivery
import database
import uvicorn
from decouple import config
from delivery.http.http import delivery_http

app = FastAPI()
delivery_http(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=int(config('PORT')))