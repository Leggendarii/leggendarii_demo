from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from app.calculator import calculate_scr


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class SCRRequest(BaseModel):
    voltage: float
    power: float
    xr: float
    frequency: float
    ssc: float


@app.get("/")
def root():
    return {
        "message": "Backend running"
    }


@app.options("/calculate")
def calculate_options():
    return {}


@app.post("/calculate")
def calculate(request: SCRRequest):

    result = calculate_scr(
        request.voltage,
        request.power,
        request.xr,
        request.frequency,
        request.ssc
    )

    return result
