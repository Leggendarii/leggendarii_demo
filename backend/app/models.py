from pydantic import BaseModel


class SCRRequest(BaseModel):
    voltage: float
    power: float
    xr: float
    frequency: float
