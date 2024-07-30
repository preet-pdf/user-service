import os
from auth0.management import Auth0
from fastapi import HTTPException

from app.models.Role import RoleAssignment
from app.models.user import ConnectionResponse, User, UserRoleResponse

APP_AUTH0_DOMAIN = os.environ.get("APP_AUTH0_DOMAIN")
APP_AUTH0_CLIENT_ID = os.environ.get("APP_AUTH0_CLIENT_ID")
AUTH0_MANAGEMENT_API = os.environ.get("AUTH0_MANAGEMENT_API")

auth0 = Auth0(APP_AUTH0_DOMAIN, AUTH0_MANAGEMENT_API )
def create_user(user: User, role_assignment: RoleAssignment):
    try:
        # Fetch the connection details
        connection = auth0.connections.get(user.connection)
        print(connection)

        # Check if the connection requires a username
        if not connection.get('options', {}).get('requires_username', False):
            user_data = user.dict(exclude={'username'})
        else:
            user_data = user.dict()
        user_data['connection'] = 'Username-Password-Authentication'

        # Create the user in Auth0
        new_user = auth0.users.create(user_data)
        user_id = new_user['user_id']
        

        # Assign the role to the user
        auth0.users.add_roles(user_id, [role_assignment.role_id])

        return UserRoleResponse(user_id=user_id, email=new_user['email'], role_id=role_assignment.role_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def list_connection():
    connections = auth0.connections.all()
    print(connections)
    return [ConnectionResponse(id=conn['id'], name=conn['name'], strategy=conn['strategy']) for conn in connections]
    