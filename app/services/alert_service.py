from app.grpc.update_alert_client import update_alert_status

async def update_alert(status: bool):
    response = await update_alert_status(status)
    return response