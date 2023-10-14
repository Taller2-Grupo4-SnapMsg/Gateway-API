# users.py
"""
This is the users' micro service represented in the gateway.
"""
from urllib.parse import quote
import requests
from fastapi import APIRouter, Header
from control.models import UserRegistration, UserLogIn
from control.utils import generate_response
from control.utils import create_header_token
from control.utils import create_user_registration_payload
from control.utils import create_header_no_token
from control.env import USERS_URL

router = APIRouter(tags=["users"])
origins = ["*"]

TIMEOUT = 20


# Route to handle user registration
@router.post("/register")
def register(user_data: UserRegistration):
    """
    Register a new user
    """
    # It's a registration here and on users_admin.py, so it's not a duplicate
    # pylint: disable=R0801:
    payload = create_user_registration_payload(user_data)
    headers_request = create_header_no_token()
    url = USERS_URL + "/register"
    response = requests.post(
        url, json=payload, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)


# Route to log in
@router.post("/login")
def login(user_data: UserLogIn):
    """
    Log in a user
    """

    payload = {"password": user_data.password, "email": user_data.email}
    headers_request = create_header_no_token()
    response = requests.post(
        USERS_URL + "/login", json=payload, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)


@router.post("/login_with_google")
def login_with_google(firebase_id_token: str = Header(...)):
    """
    Log in a user with Google
    """
    headers_request = create_header_token(firebase_id_token)
    response = requests.post(
        USERS_URL + "/login_with_google",
        headers=headers_request,
        timeout=TIMEOUT,
    )
    return generate_response(response)


# Route to get a user either by email or by username
@router.get("/users/find")
def get_user(email: str = None, username: str = None, token: str = Header(...)):
    """
    Get a user either by email or by username
    """
    headers_request = create_header_token(token)

    url = USERS_URL + "/users/find"
    if email:
        url += f"?email={email}"
    if username:
        url += f"?username={username}"
    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)
    return generate_response(response)


@router.get("/users/interests")
def get_interests(token: str = Header(...)):
    """
    Get a user either by email or by username
    """
    headers_request = create_header_token(token)

    url = USERS_URL + "/users/interests"

    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)
    return generate_response(response)


@router.delete("/users/{email}")
def delete_user(email: str, token: str = Header(...)):
    """
    Delete a user
    """
    headers_request = create_header_token(token)
    params = {"email": email}
    url = f"{USERS_URL}/users/{quote(params['email'])}"

    response = requests.delete(
        url, params=params, headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)


# Route to get a user's information by token
@router.get("/get_user_by_token")
def get_user_by_token(token: str = Header(...)):
    """
    Get a user's information by token
    """
    headers_request = create_header_token(token)

    response = requests.get(
        USERS_URL + "/get_user_by_token", headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)


@router.get("/user")
def get_user_by_token_with_id(token: str = Header(...)):
    """
    Get a user's information by token
    """
    headers_request = create_header_token(token)

    response = requests.get(
        USERS_URL + "/user", headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)


@router.get("/user/search/{username}")
def search_users_by_username(
    username: str, offset: int, ammount: int, token: str = Header(...)
):
    """
    Get a user's information by token
    """
    headers_request = create_header_token(token)
    params = {"username": username, "offset": offset, "ammount": ammount}
    url = f"{USERS_URL}/user/search/\
        {quote(params['username'])}?offset={params['offset']}&ammount={params['ammount']}"

    response = requests.get(
        url, params=params, headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)
