from fastapi import FastAPI
from pydantic import BaseModel

from calculations import calculate_scr


app = FastAPI()


class SCRRequest(BaseModel):
    voltage: float
    power: float
    xr: float
    frequency: float


@app.get("/")
def root():
    return {
        "message": "Backend running"
    }


@app.post("/calculate")
def calculate(request: SCRRequest):

    result = calculate_scr(
        request.voltage,
        request.power,
        request.xr,
        request.frequency
    )

    return result
