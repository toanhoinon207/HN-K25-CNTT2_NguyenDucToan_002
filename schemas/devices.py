from typing import List
from pydantic import BaseModel, Field
from schemas.device_types import DeviceTypes

class DeviceCreate(BaseModel):
    device_code: str = Field(..., min_length = 4, max_length = 10)
    price: float = Field(..., gt = 0)
    device_type_id: int = Field(...)

class DeviceResponse(BaseModel):
    id: int
    device_code: str
    price: float
    device_type: List[DeviceTypes]