# users_admin.py
"""
Module for the endpoints of the users' API that are only available for admins
"""

from urllib.parse import quote
import requests
from fastapi import APIRouter, Header
from control.models import UserLogIn, UserRegistration
from control.utils import generate_response
from control.utils import create_header_token
from control.utils import create_user_registration_payload
from control.utils import create_header_no_token
from control.env import USERS_URL

router = APIRouter()
origins = ["*"]

TIMEOUT = 20


# Route for admin registration
@router.post("/register_admin")
def register_admin(user_data: UserRegistration):
    """
    Register a new admin
    """
    payload = create_user_registration_payload(user_data)
    headers_request = create_header_no_token()
    response = requests.post(
        USERS_URL + "/register_admin",
        json=payload,
        headers=headers_request,
        timeout=TIMEOUT,
    )

    return generate_response(response)


# Route for admin log in
@router.post("/login_admin")
def login_admin(user_data: UserLogIn):
    """
    Log in an admin
    """
    payload = {"password": user_data.password, "email": user_data.email}
    headers_request = create_header_no_token()
    # call to user's API
    response = requests.post(
        USERS_URL + "/login_admin",
        json=payload,
        headers=headers_request,
        timeout=TIMEOUT,
    )

    return generate_response(response)


# Route to update a user's blocked status
@router.put("/users/block/{email}")
def block_user(email: str, blocked: bool, token: str = Header(...)):
    """
    Update a user's blocked status
    """
    headers_request = create_header_token(token)
    params = {"email": email, "blocked": blocked}
    url = f"{USERS_URL}/users/block/{quote(params['email'])}"

    response = requests.put(
        url, params=params, headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)


# Route to making a user an admin
@router.put("/users/{email}/make_admin")
def make_admin(email: str, token: str = Header(...)):
    """
    Make a user an admin
    """
    headers_request = create_header_token(token)
    params = {"email": email}
    url = f"{USERS_URL}/users/{quote(params['email'])}/make_admin"

    response = requests.put(
        url, params=params, headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)


# Route to making an admin a normal user
@router.put("/users/{email}/remove_admin")
def remove_admin(email: str, token: str = Header(...)):
    """
    Make an admin a normal user
    """
    headers_request = create_header_token(token)
    params = {"email": email}
    url = f"{USERS_URL}/users/{quote(params['email'])}/remove_admin"

    response = requests.put(
        url, params=params, headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)


# Route to delete a user, this one can be used by the user itself
@router.delete("/users/{email}")
def delete_user(email: str, token: str = Header(...)):
    """
    Delete a user, this one can be used by the user itself
    """
    headers_request = create_header_token(token)
    params = {"email": email}
    url = f"{USERS_URL}/users/{quote(params['email'])}"

    response = requests.delete(
        url, params=params, headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)


# Route to get all users
@router.get("/users")
def get_all_users(token: str = Header(...)):
    """
    Get all users
    """
    headers_request = create_header_token(token)
    url = USERS_URL + "/users"
    # call to user's API
    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


# Route to get all following relations
@router.get("/following")
def get_all_following(token: str = Header(...)):
    """
    Get all following relations
    """
    headers_request = create_header_token(token)
    url = USERS_URL + "/following"
    # call to user's API
    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)
