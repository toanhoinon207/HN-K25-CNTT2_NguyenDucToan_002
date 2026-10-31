from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.device_types import DeviceTypesModel

class DevicesModel(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key = True, index = True)
    device_code = Column(String(10), unique = True, nullable = False)
    price = Column(Float, nullable = False)
    device_type_id = Column(Integer, ForeignKey(DeviceTypesModel.id), nullable = False,)
    device_type = relationship("DeviceTypesModel", back_populates = "device")