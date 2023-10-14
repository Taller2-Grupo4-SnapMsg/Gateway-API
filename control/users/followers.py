# followers.py
"""
This is the users' followers micro-service represented in the gateway.
"""
from urllib.parse import quote
import requests
from fastapi import APIRouter, Header
from control.utils import generate_response
from control.utils import create_header_token
from control.env import USERS_URL

router = APIRouter(tags=["followers"])
origins = ["*"]


TIMEOUT = 20


# Route to create a follow:
@router.post("/follow/{email}")
def create_follow(email: str, token: str = Header(...)):
    """
    Create a follow
    """
    headers_request = create_header_token(token)
    email = {"email_following": email}
    url = f"{USERS_URL}/follow/{quote(email['email_following'])}"

    response = requests.post(
        url, params=email, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)


# Route to get all followers from an email
@router.get("/followers/{email}")
def get_followers(email: str, token: str = Header(...)):
    """
    Get all followers from an email
    """
    headers_request = create_header_token(token)
    email = {"email": email}
    url = f"{USERS_URL}/followers/{quote(email['email'])}"

    response = requests.get(url, params=email, headers=headers_request, timeout=TIMEOUT)
    return generate_response(response)


# Route to know if a user is following a given email
@router.get("/is_following/{email}")
def is_following(email: str, token: str = Header(...)):
    """
    Checks if the user that is identified by the token
    is following the user identified by the email
    """
    headers_request = create_header_token(token)
    email = {"email_following": email}
    url = f"{USERS_URL}/is_following/{quote(email['email_following'])}"

    response = requests.get(url, params=email, headers=headers_request, timeout=TIMEOUT)
    return generate_response(response)


@router.get("/is_follower/{email}")
def get_is_follower(email_follower: str, token: str = Header(...)):
    """
    Checks if the user that is identified by the token
    is being followed by the user identified by the email
    """
    headers_request = create_header_token(token)
    email = {"email_follower": email_follower}
    url = f"{USERS_URL}/is_follower/{quote(email['email_follower'])}"

    response = requests.get(url, params=email, headers=headers_request, timeout=TIMEOUT)
    return generate_response(response)


# Route to get all following from an email
@router.get("/following/{email}")
def get_following(email: str, token: str = Header(...)):
    """
    Get all following from an email
    """
    headers_request = create_header_token(token)
    email = {"email": email}
    url = f"{USERS_URL}/following/{quote(email['email'])}"

    response = requests.get(url, params=email, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


# Route to get the follower count of a given email
@router.get("/follow/{email}/count")
def get_follow_count(email: str, token: str = Header(...)):
    """
    Get the follower count of a given email
    """
    headers_request = create_header_token(token)
    email = {"email": email}
    url = f"{USERS_URL}/follow/{quote(email['email'])}/count"

    response = requests.get(url, params=email, headers=headers_request, timeout=TIMEOUT)
    return generate_response(response)


# Route to get the following count of a given email
@router.get("/following/{email}/count")
def get_following_count(email: str, token: str = Header(...)):
    """
    Get the following count of a given email
    """
    headers_request = create_header_token(token)
    email = {"email": email}
    url = f"{USERS_URL}/following/{quote(email['email'])}/count"

    response = requests.get(url, params=email, headers=headers_request, timeout=TIMEOUT)
    return generate_response(response)


# Route to delete a follow
@router.delete("/unfollow")
def unfollow_email(email_unfollowing: str, token: str = Header(...)):
    """
    Delete a follow
    """
    headers_request = create_header_token(token)
    email = {"email_unfollowing": email_unfollowing}

    response = requests.delete(
        USERS_URL + "/unfollow", params=email, headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)
