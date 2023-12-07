# likes.py
"""
Module for the endpoints of the likes
"""
import requests
from fastapi import APIRouter, Header
from control.utils import generate_response
from control.utils import create_header_token
from control.env import SNAPMSG_URL

router = APIRouter(tags=["Likes"])
origins = ["*"]

TIMEOUT = 20


@router.post("/likes/{post_id}")
def create_like(post_id: int, token: str = Header(...)):
    """
    Create a like
    """
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/likes/{post_id}"

    response = requests.post(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


@router.delete("/likes/{post_id}")
def delete_like(post_id: int, token: str = Header(...)):
    """
    Delete a like
    """
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/likes/{post_id}"

    response = requests.delete(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)
