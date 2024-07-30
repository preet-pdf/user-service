from http.client import HTTPException
from typing import Annotated
from fastapi import APIRouter, Depends, Query
from app.models import Role
from app.services.role_service import assign_permission, get_all_roles, create_role, list_permission

router = APIRouter()

@router.get("/get_role", tags=["Role"])
async def get_role():
    response = await get_all_roles()
    return {"response": response}

@router.post("/create_role", tags=["Role"])
async def create_rol(role: Role.Role):
    response = create_role(role)
    return Role.RoleResponse(id=response['id'], name=response['name'], description=response['description'])

@router.post("/assign-permission/{role_id}", response_model=Role.MessageResponse, tags=["Role"])
async def assign_permissio(role_id: str, permission: Role.Permission):
    response = await get_all_roles()
    role_found = False
    for role in response['roles']:
        if role['id'] == role_id:
            role_found = True
            response = assign_permission(role_id, permission)
            return response
    if not role_found:
        raise HTTPException(status_code=400, detail='role not found')
    
@router.post("/create_role_and_assign_permission", tags=["Role"])
async def create_role_and_assign_permission(role: Role.Role, permission: list[Role.Permission]):
    response = create_role(role)
    for perm in permission:
        assign_permission(response['id'], perm)
    return {"response": 'Role Created Successfully and Assign Permission to that Role'}

@router.post("/list-permissions", tags=["Role"])
def list_permissions():
    response = list_permission()
    return response