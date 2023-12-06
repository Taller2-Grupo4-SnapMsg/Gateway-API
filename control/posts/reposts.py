# reposts.py
"""
Module for the endpoints of the reposts
"""
import requests
from fastapi import APIRouter, Header
from control.utils import generate_response
from control.utils import create_header_token
from control.env import SNAPMSG_URL

router = APIRouter(tags=["Reposts"])
origins = ["*"]

TIMEOUT = 20


### QUEDA PROBAR
@router.post("/reposts/{post_id}")
def create_repost(post_id: int, token: str = Header(...)):
    """
    Create a repost
    """
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/reposts/{post_id}"

    response = requests.post(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


### QUEDA PROBAR
@router.delete("/reposts/from_post/{post_id}")
def delete_respost_from_post(post_id: int, token: str = Header(...)):
    """
    Delete a repost
    """
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/reposts/from_post/{post_id}"

    response = requests.delete(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


### QUEDA PROBAR
@router.delete("/reposts/{repost_id}")
def delete_repost(repost_id: int, token: str = Header(...)):
    """
    Delete a repost
    """
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/reposts/{repost_id}"

    response = requests.delete(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)
