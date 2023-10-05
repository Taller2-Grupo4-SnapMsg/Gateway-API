# users.py
"""
This is the users' micro service represented in the gateway.
"""
import requests
from fastapi import APIRouter, Header
from pydantic import BaseModel
from control.utils import generate_response
from control.utils import create_header_token
from control.env import USERS_URL

router = APIRouter()
origins = ["*"]

TIMEOUT = 20


class UserRegistration(BaseModel):
    """
    This class is a Pydantic model for the request body.
    """

    password: str
    email: str
    name: str
    last_name: str
    username: str
    date_of_birth: str


class UserLogIn(BaseModel):
    """
    This class is a Pydantic model for the request body.
    """

    email: str
    password: str


# Route to handle user registration
@router.post("/register")
def register(user_data: UserRegistration):
    """
    Register a new user
    """
    payload = {
        "password": user_data.password,
        "email": user_data.email,
        "name": user_data.name,
        "last_name": user_data.last_name,
        "username": user_data.username,
        "date_of_birth": user_data.date_of_birth,
    }
    headers_request = {"accept": "application/json", "Content-Type": "application/json"}
    # call to user's API
    response = requests.post(
        USERS_URL + "/register", json=payload, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)


# Route to log in
@router.post("/login")
def login(user_data: UserLogIn):
    """
    Log in a user
    """
    payload = {"password": user_data.password, "email": user_data.email}
    headers_request = {"accept": "application/json", "Content-Type": "application/json"}
    # call to user's API
    response = requests.post(
        USERS_URL + "/login", json=payload, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)


# Route for admin log in
@router.post("/login_admin")
def login_admin(user_data: UserLogIn):
    """
    Log in an admin
    """
    payload = {"password": user_data.password, "email": user_data.email}
    headers_request = {"accept": "application/json", "Content-Type": "application/json"}
    # call to user's API
    response = requests.post(
        USERS_URL + "/login_admin",
        json=payload,
        headers=headers_request,
        timeout=TIMEOUT,
    )

    return generate_response(response)


# Route for admin registration
@router.post("/register_admin")
def register_admin(user_data: UserRegistration):
    """
    Register a new admin
    """
    payload = {
        "password": user_data.password,
        "email": user_data.email,
        "name": user_data.name,
        "last_name": user_data.last_name,
        "username": user_data.username,
        "date_of_birth": user_data.date_of_birth,
    }
    headers_request = {"accept": "application/json", "Content-Type": "application/json"}
    # call to user's API
    response = requests.post(
        USERS_URL + "/register_admin",
        json=payload,
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
    # call to user's API
    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)
    return generate_response(response)
