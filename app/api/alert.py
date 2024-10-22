from fastapi import APIRouter, Depends
from app.services.alert_service import update_alert
from ..security.dependencies import PermissionsValidator

router = APIRouter()

@router.post("/update_alert", tags=["GRPC Call"], dependencies=[Depends(PermissionsValidator(["app-admin:update-alert"]))])
async def update_alert_status(status: bool):
    print(status)
    response = await update_alert(status)
    return {"response": response}
