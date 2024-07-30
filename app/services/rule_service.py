from app.grpc.update_rule_client import update_rule as grpc_update_rule

async def update_rule(status: bool):
    response = await grpc_update_rule(status)
    return response
