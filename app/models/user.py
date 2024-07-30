from pydantic import BaseModel, EmailStr, Field, constr
from typing import List, Optional

class User(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    connection: str
    username: Optional[str] = Field(..., min_length=3, max_length=10)
    given_name: Optional[str]
    family_name: Optional[str]
    name: Optional[str]
    nickname: Optional[str]
    picture: Optional[str]
    user_metadata: Optional[dict]
    app_metadata: Optional[dict]

class UserResponse(BaseModel):
    user_id: str
    email: str

class UserRoleResponse(BaseModel):
    user_id: str
    email: str
    role_id: str

class ConnectionResponse(BaseModel):
    id: str
    name: str
    strategy: str
