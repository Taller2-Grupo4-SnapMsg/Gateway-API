# users.py
"""
This is the users' micro service represented in the gateway.
"""
from urllib.parse import quote
import requests
from fastapi import APIRouter, Header, HTTPException, Query
from control.models import UserRegistration, UserLogIn
from control.utils import generate_response
from control.utils import create_header_token
from control.utils import create_header_biometric_token_and_user_token
from control.utils import create_header_biometric_token
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
    if response.status_code == 201:
        data = response.json()
        return data
    raise HTTPException(
        status_code=response.status_code, detail=response.json().get("detail")
    )


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
    headers_request = create_header_no_token()
    headers_request["firebase-id-token"] = firebase_id_token
    response = requests.post(
        USERS_URL + "/login_with_google",
        headers=headers_request,
        timeout=TIMEOUT,
    )
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


@router.get("/user/search/{query}")
def search_users(
    query: str,
    offset=Query(default=0, description="Offset of the search."),
    ammount=Query(default=10, description="Ammount of users to return."),
    in_followers: bool = Query(
        False, title="in_followers", description="search in followers"
    ),
    token: str = Header(...),
):
    """
    Searches the users by username, name, or surname.
    """
    headers_request = create_header_token(token)
    params = {
        "query": query,
        "offset": int(offset),
        "ammount": int(ammount),
        "in_followers": in_followers,
    }
    # pylint: disable=C0301
    # We can't do anything about the length of the url, and we can't use \ to break the line
    # Because it would break the url
    url = f"{USERS_URL}/user/search/{quote(params['query'])}?offset={params['offset']}&ammount={params['ammount']}&in_followers={params['in_followers']}"

    response = requests.get(
        url, params=params, headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)


@router.post("/user/biometric_token")
def set_biometric_token(token: str = Header(...)):
    """
    Set the biometric token of the user
    """
    headers_request = create_header_token(token)

    response = requests.post(
        USERS_URL + "/user/biometric_token", headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)


@router.delete("/user/delete_biometric_token")
def delete_biometric_token(
    token: str = Header(...), biometric_token: str = Header(...)
):
    """
    Delete the biometric token of the user
    """
    headers_request = create_header_biometric_token_and_user_token(
        token, biometric_token
    )

    response = requests.delete(
        USERS_URL + "/user/delete_biometric_token",
        headers=headers_request,
        timeout=TIMEOUT,
    )
    return generate_response(response)


@router.post("/login_with_biometrics")
def login_with_biometrics(biometric_token: str = Header(...)):
    """
    Log in a user with biometrics
    """
    headers_request = create_header_biometric_token(biometric_token)

    response = requests.post(
        USERS_URL + "/login_with_biometrics",
        headers=headers_request,
        timeout=TIMEOUT,
    )
    return generate_response(response)


@router.get("/users/username/{username}")
def get_user_by_username_from_user(username: str, token: str = Header(...)):
    """
    Get a user either by email or by username
    """
    headers_request = create_header_token(token)
    url = f"{USERS_URL}/users/username/{username}"

    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)
    return generate_response(response)
