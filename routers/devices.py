from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services.device import create_device, get_device
from schemas.response import success_response
from schemas.devices import DeviceCreate

router = APIRouter(prefix = "/devices", tags = ["Devices"])

@router.post("/")
def add_device(device_data: DeviceCreate, db: Session = Depends(get_db)):
    data = create_device(db, device_data)

    return success_response(
        201,
        "Thêm thiết bị thành công!",
        data
    )

@router.get("/")
def show_device(db: Session = Depends(get_db)):
    data = get_device(db)

    return success_response(
        200,
        "Lấy thiết bị thành công!",
        data
    )