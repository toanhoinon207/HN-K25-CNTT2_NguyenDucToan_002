from fastapi import HTTPException, status
from models.device_types import DeviceTypesModel

def remove_device_type(db, device_type_id):
    device_type = db.query(DeviceTypesModel).filter(DeviceTypesModel.id == device_type_id).first()

    if device_type is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Không tìm thấy loại thiết bị!"
        )


    db.delete(device_type)
    db.commit()

    return device_type