# users_admin.py
"""
Module for the endpoints of the users' API that are only available for admins
"""

from urllib.parse import quote
import requests
from fastapi import APIRouter, Header, Query
from control.models import UserLogIn
from control.utils import generate_response
from control.utils import create_header_token
from control.utils import create_header_no_token
from control.env import USERS_URL
from control.env import ADMINS_URL

router = APIRouter(tags=["admin"])
origins = ["*"]

TIMEOUT = 20


# Route for admin registration
@router.post("/register_admin")
def register_admin(user_data: UserLogIn):
    """
    Register a new admin
    """
    payload = {"email": user_data.email, "password": user_data.password}
    headers_request = create_header_no_token()
    response = requests.post(
        ADMINS_URL + "/admin",
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

    response = requests.post(
        ADMINS_URL + "/admin/login",
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


@router.get("/admin/find_users/{username}")
def find_users(username: str, start: int, ammount: int, token: str = Header(...)):
    """
    Find users by username
    """
    headers_request = create_header_token(token)
    params = {"username": username, "start": start, "ammount": ammount}
    # pylint: disable=C0301
    # We can't do anything about the length of the url, and we can't use \ to break the line
    # Because it would break the url
    url = f"{USERS_URL}/admin/find_users/{quote(params['username'])}?start={params['start']}&ammount={params['ammount']}"
    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)
    return generate_response(response)


@router.get("/admin/is_admin")
def validate_admin_token(token: str = Header(...)):
    """
    Validate admin token
    """
    headers_request = create_header_token(token)
    url = ADMINS_URL + "/admin"
    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)
    return generate_response(response)


# Route to get all users
@router.get("/users")
def get_all_users(
    start: int = Query(default=0, description="Offset of the search."),
    ammount: int = Query(default=10, description="Ammount of users to return."),
    token: str = Header(...),
):
    """
    Get all users
    """
    headers_request = create_header_token(token)
    url = USERS_URL + "/users" + f"?start={start}&ammount={ammount}"

    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


@router.get("/users/{query}")
def get_users_by_query(
    query: str,
    start: int = Query(default=0, description="Offset of the search."),
    ammount: int = Query(default=10, description="Ammount of users to return."),
    token: str = Header(...),
):
    """
    Get users by a query that searches for email, username, lastname, firstname
    """
    headers_request = create_header_token(token)
    url = USERS_URL + "/users/" + query + f"?start={start}&ammount={ammount}"

    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


# Route to get a user either by email or by username
@router.get("/users/admin/find")
def get_user(email: str = None, username: str = None, token: str = Header(...)):
    """
    Get a user either by email or by username
    """
    headers_request = create_header_token(token)

    url = USERS_URL + "/users/admin/find"
    if email:
        url += f"?email={email}"
    if username:
        url += f"?username={username}"
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

    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)
