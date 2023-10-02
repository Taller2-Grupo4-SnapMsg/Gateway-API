# users.py
"""
This is the users' micro service represented in the gateway.
"""
import os
import requests
from fastapi import APIRouter, Header, Response
from pydantic import BaseModel

router = APIRouter()
origins = ["*"]


USERS_URL = os.environ.get("USERS_URL")
if USERS_URL is None:
    print("You forgot to set USERS_URL!")

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
    return requests.post(
        USERS_URL + "/register", json=payload, headers=headers_request, timeout=TIMEOUT
    ).json()


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
    response = Response(content=response.content, status_code=response.status_code)
    return response


# Route to create a follow:
@router.post("/follow/{email}")
def create_follow(email: str, token: str = Header(...)):
    """
    Create a follow
    """
    headers_request = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "token": token,
    }
    email = {"email_following": email}
    # call to user's API
    response = requests.post(
        USERS_URL + "/follow", params=email, headers=headers_request, timeout=TIMEOUT
    )
    response = Response(content=response.content, status_code=response.status_code)
    return response
