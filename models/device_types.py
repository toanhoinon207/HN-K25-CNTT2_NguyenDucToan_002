from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class DeviceTypesModel(Base):
    __tablename__ = "device_types"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(50), unique = True, nullable = False)
    device = relationship("DevicesModel", back_populates = "device_type")