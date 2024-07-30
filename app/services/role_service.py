
from dotenv import load_dotenv
import os
from auth0.management import Auth0
from fastapi import HTTPException

from app.models import Role
load_dotenv()
APP_AUTH0_DOMAIN = os.environ.get("APP_AUTH0_DOMAIN")
APP_AUTH0_CLIENT_ID = os.environ.get("APP_AUTH0_CLIENT_ID")
AUTH0_MANAGEMENT_API = os.environ.get("AUTH0_MANAGEMENT_API")

auth0 = Auth0(APP_AUTH0_DOMAIN, AUTH0_MANAGEMENT_API )

async def get_all_roles():
    roles = auth0.roles.list()
    return roles

def create_role(role: Role):
    try:
        new_role = auth0.roles.create({
            'name': role.name,
            'description': role.description
        })
        return new_role
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def assign_permission(role_id: str, permission: Role.Permission):
    try:
        resource_servers = auth0.resource_servers.get_all()
        valid_identifiers = {server['identifier']: server['scopes'] for server in resource_servers}
        
        if permission.resource_server_identifier not in valid_identifiers:
            raise HTTPException(status_code=404, detail=f"Resource server does not exist: '{permission.resource_server_identifier}'")
        
        scope_of_valid_identifiers = valid_identifiers[permission.resource_server_identifier]
        if permission.permission_name not in [v['value'] for v in scope_of_valid_identifiers]:
            raise HTTPException(status_code=404, detail=f"Resource server scope does not exist: '{permission.permission_name}'")
        
        auth0.roles.add_permissions(role_id, [{
            'resource_server_identifier': permission.resource_server_identifier,
            'permission_name': permission.permission_name
        }])
        return Role.MessageResponse(message="Permission assigned successfully")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
def list_permission():
    resource_servers = auth0.resource_servers.get_all()
    valid_identifiers = {server['identifier']: server['scopes'] for server in resource_servers}
    return valid_identifiers