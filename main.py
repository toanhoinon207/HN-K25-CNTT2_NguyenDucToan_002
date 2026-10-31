from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from database import engine, Base
from schemas.response import error_response
from models import DevicesModel, DeviceTypesModel
from routers.devices import router as DevicesRouter
from routers.device_types import router as DeviceTypesRouter

app = FastAPI()

Base.metadata.create_all(bind = engine)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code = exc.status_code,
        content = error_response(
            exc.status_code,
            True,
            str(exc.detail)
        )
    )

@app.get("/")
def check_connect():
    return {
        "message": "Kết nối thành công"
    }

app.include_router(DevicesRouter)
app.include_router(DeviceTypesRouter)