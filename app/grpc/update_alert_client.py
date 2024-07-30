import grpc
from app.grpc.update_rule_pb2 import AlertRequest
from app.grpc.update_rule_pb2_grpc import UpdateAlertStatusServiceStub

async def update_alert_status(status: bool):
    async with grpc.aio.insecure_channel('localhost:9090') as channel:
        stub = UpdateAlertStatusServiceStub(channel)
        request_iterator = iter([AlertRequest(status=status)])
        async for response in stub.UpdateAlertStatus(request_iterator):
            return response.response
