from fastapi import HTTPException
from schemas.devices import DeviceCreate
from models.device_types import DeviceTypesModel
from models.devices import DevicesModel

def create_device(db, device_data):
    is_existed = db.query(DeviceTypesModel).filter(DeviceTypesModel.id == device_data.device_type_id).first()

    if is_existed is None:
        raise HTTPException(
            status_code = 404,
            detail = "Không tìm thấy loại thiết bị!"
        )

    new_device = DevicesModel(**device_data.model_dump())
    
    db.add(new_device)
    db.commit()
    db.refresh(new_device)

    return new_device

def get_device(db):
    device = db.query(DevicesModel).all()

    return device