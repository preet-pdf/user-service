from fastapi import APIRouter, Depends
from app.services.alert_service import update_alert

router = APIRouter()

@router.post("/update_alert", tags=["GRPC Call"])
async def update_alert_status(status: bool):
    print(status)
    response = await update_alert(status)
    return {"response": response}
