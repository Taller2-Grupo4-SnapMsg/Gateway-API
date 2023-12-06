# pylint: disable=R0801
# posts_admin.py
"""
Module for the endpoints of the posts' API for admins
"""
from urllib.parse import quote
import requests
from fastapi import APIRouter, Header, Query
from control.utils import generate_response
from control.utils import create_header_token
from control.env import SNAPMSG_URL

router = APIRouter(tags=["Admin"])
origins = ["*"]

TIMEOUT = 20


### QUEDA PROBAR
@router.post("/admin/health")
def get_service_health_and_description():
    """
    Get service health and description
    """
    url = f"{SNAPMSG_URL}/admin/health"
    response = requests.post(url, timeout=TIMEOUT)
    return generate_response(response)


### QUEDA PROBAR
@router.get("/posts/admin/all")
def get_posts_for_admin(
    start: int = Query(0, title="start", description="start for pagination"),
    ammount: int = Query(10, title="ammount", description="ammount of posts"),
    token: str = Header(...),
):
    """
    Get all posts for admin
    """
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/posts/admin/all?start={start}&ammount={ammount}"

    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


### QUEDA PROBAR
@router.get("/posts/admin/user")
def get_posts_for_admin_user_id(
    email: str,
    start: int = Query(0, title="start", description="start for pagination"),
    ammount: int = Query(10, title="ammount", description="ammount of posts"),
    token: str = Header(...),
):
    """
    Get all posts for admin from a user
    """
    headers_request = create_header_token(token)
    url = (
        f"{SNAPMSG_URL}/posts/admin/user?email={email}&start={start}&ammount={ammount}"
    )

    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


### QUEDA PROBAR
@router.get("/posts/admin/search/{text}")
def get_posts_for_admin_search(
    text: str,
    offset=Query(0, title="offset", description="offset for pagination"),
    amount=Query(10, title="ammount", description="max ammount of users to return"),
    token: str = Header(...),
):
    """
    Get posts for admin search
    """
    headers_request = create_header_token(token)
    params = {
        "text": text,
        "offset": int(offset),
        "ammount": int(amount),
    }
    # pylint: disable=line-too-long
    url = f"{SNAPMSG_URL}/posts/admin/search/{quote(params['text'])}?offset={params['offset']}&ammount={params['ammount']}"

    response = requests.get(
        url, params=params, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)
