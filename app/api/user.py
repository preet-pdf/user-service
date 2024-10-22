from typing import Annotated, List
from fastapi import APIRouter, Depends, Query
from app.models.Role import RoleAssignment
from app.models.user import ConnectionResponse, User, UserRoleResponse
from app.services.user_service import create_user, list_connection
from ..security.dependencies  import PermissionsValidator

router = APIRouter()

@router.post("/create-user", response_model=UserRoleResponse, tags=["Users"], dependencies=[Depends(PermissionsValidator(["admin:alert"]))])
def create_user_resource(user: User, role_assignment: RoleAssignment):
    response = create_user(user, role_assignment)
    return response

@router.get("/list-connections", response_model=List[ConnectionResponse], tags=["Users"], dependencies=[Depends(PermissionsValidator(["app-admin:alert-connection"]))])
def list_connections():
    response = list_connection()
    return response