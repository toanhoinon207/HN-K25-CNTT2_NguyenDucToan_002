from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services.device_type import remove_device_type
from schemas.response import success_response
from schemas.devices import DeviceCreate

router = APIRouter(prefix = "/device_types", tags = ["DeviceTypes"])

@router.delete("/")
def delete_device_type(device_type_id: int, db: Session = Depends(get_db)):
    data = remove_device_type(db, device_type_id)

    return success_response(
        200,
        "Xoá loại thiết bị thành công",
        data
    )