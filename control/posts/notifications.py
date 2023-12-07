# notifications.py
"""
Module for the endpoints of the notifications
"""
import requests
from fastapi import APIRouter, Header
from control.models import NotificationRequest
from control.utils import create_notification_payload
from control.utils import generate_response
from control.utils import create_header_token
from control.env import SNAPMSG_URL

router = APIRouter(tags=["Notifications"])
origins = ["*"]

TIMEOUT = 20


@router.post("/notifications/save/{device_token}")
def save_device_token(device_token: str, token: str = Header(...)):
    """
    Save device token
    """
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/notifications/save/{device_token}"

    response = requests.post(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


@router.delete("/notifications/{device_token}")
def delete_device_token(device_token: str, token: str = Header(...)):
    """
    Delete device token
    """
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/notifications/{device_token}"

    response = requests.delete(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


@router.post("/notifications/push", tags=["Notifications"])
def api_send_notificacion(
    notificacion_request: NotificationRequest, token: str = Header(...)
):
    """
    Send a notification
    """
    headers_request = create_header_token(token)
    payload = create_notification_payload(notificacion_request)
    url = f"{SNAPMSG_URL}/notifications/push"

    response = requests.post(
        url, json=payload, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)
