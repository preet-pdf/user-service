from fastapi import APIRouter, Depends
from app.services.rule_service import update_rule

router = APIRouter()

@router.post("/update_rule", tags=["GRPC Call"])
async def update_rule_endpoint(status: bool):
    print(status)
    response = await update_rule(status)
    return {"response": response}
