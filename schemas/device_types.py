from pydantic import BaseModel

class DeviceTypes(BaseModel):
    id: int
    name: str