from pydantic import BaseModel

class Role(BaseModel):
    name: str
    description: str

class RoleResponse(BaseModel):
    id: str
    name: str
    description: str

class MessageResponse(BaseModel):
    message: str

class Permission(BaseModel):
    resource_server_identifier: str
    permission_name: str


class RoleAssignment(BaseModel):
    role_id: str