from fastapi import APIRouter, Depends
from app.services.rule_service import update_rule
from ..security.dependencies import PermissionsValidator

router = APIRouter()

@router.post("/update_rule", tags=["GRPC Call"], dependencies=[Depends(PermissionsValidator(["app-admin:update-rule"]))])
async def update_rule_endpoint(status: bool):
    print(status)
    response = await update_rule(status)
    return {"response": response}
