# favorites.py
"""
Module for the endpoints of the favorites
"""
import requests
from fastapi import APIRouter, Header
from control.utils import generate_response
from control.utils import create_header_token
from control.env import SNAPMSG_URL

router = APIRouter(tags=["Favorites"])
origins = ["*"]

TIMEOUT = 20


@router.post("/favorites/{post_id}")
def create_favorite(post_id: int, token: str = Header(...)):
    """
    Create a favorite
    """
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/favorites/{post_id}"

    response = requests.post(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


@router.delete("/favorites/{post_id}")
def delete_favorite(post_id: int, token: str = Header(...)):
    """
    Delete a favorite
    """
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/favorites/{post_id}"

    response = requests.delete(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


@router.get(
    "/favorites/profile/{user_visited_email}/oldest_date/{oldest_date_str}"
    "/amount/{amount}",
    tags=["Favorites"],
)
def get_favorites_from_user_visited(
    user_visited_email: str,
    oldest_date_str: str,
    amount: int,
    token: str = Header(...),
):
    """
    Get favorites from a user
    """
    headers_request = create_header_token(token)
    # pylint: disable=line-too-long
    url = f"{SNAPMSG_URL}/favorites/profile/{user_visited_email}/oldest_date/{oldest_date_str}/amount/{amount}"

    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)
