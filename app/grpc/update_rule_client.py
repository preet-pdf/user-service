import grpc
from app.grpc.update_rule_pb2 import UpdateRuleRequest
from app.grpc.update_rule_pb2_grpc import UpdateRuleServiceStub

async def update_rule(status: bool):
    async with grpc.aio.insecure_channel('localhost:9090') as channel:
        stub = UpdateRuleServiceStub(channel)
        request_iterator = iter([UpdateRuleRequest(status=status)])
        async for response in stub.UpdateRule(request_iterator):
            return response.response