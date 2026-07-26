from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .models import SCRRequest
from .calculator import calculate_scr


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Backend is running"}


@app.post("/calculate")
def calculate(request: SCRRequest):

    result = calculate_scr(
        request.voltage,
        request.power,
        request.xr,
        request.frequency
    )

    return result
