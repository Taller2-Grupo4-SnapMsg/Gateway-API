# users_put.py
"""
This is the users' micro service's put methods.
"""
import requests
from fastapi import APIRouter, Header
from control.utils import generate_response
from control.utils import create_header_token
from control.env import USERS_URL

router = APIRouter()
origins = ["*"]

TIMEOUT = 20


# Route to update a user's password
@router.put("/users/password")
def change_password(new_password: str, token: str = Header(...)):
    """
    Update a user's password
    """
    headers_request = create_header_token(token)
    new_password = {"new_password": new_password}
    url = USERS_URL + "/users/password"

    response = requests.put(
        url, params=new_password, headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)


# Route to update a user's bio
@router.put("/users/bio")
def change_bio(new_bio: str, token: str = Header(...)):
    """
    Update a user's bio
    """
    headers_request = create_header_token(token)
    new_bio = {"new_bio": new_bio}
    url = USERS_URL + "/users/bio"

    response = requests.put(
        url, params=new_bio, headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)


# Route to update a user's avatar
@router.put("/users/avatar")
def change_avatar(new_avatar: str, token: str = Header(...)):
    """
    Update a user's avatar
    """
    headers_request = create_header_token(token)
    new_avatar = {"new_avatar": new_avatar}
    url = USERS_URL + "/users/avatar"

    response = requests.put(
        url, params=new_avatar, headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)


# Route to update a user's name
@router.put("/users/name")
def change_name(new_name: str, token: str = Header(...)):
    """
    Update a user's name
    """
    headers_request = create_header_token(token)
    new_name = {"new_name": new_name}
    url = USERS_URL + "/users/name"

    response = requests.put(
        url, params=new_name, headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)


# Route to update a user's date of birth
@router.put("/users/date_of_birth")
def change_date_of_birth(new_date_of_birth: str, token: str = Header(...)):
    """
    Update a user's date of birth
    """
    headers_request = create_header_token(token)
    new_date_of_birth = {"new_date_of_birth": new_date_of_birth}
    url = USERS_URL + "/users/date_of_birth"

    response = requests.put(
        url, params=new_date_of_birth, headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)


# Route to update a user's last name
@router.put("/users/last_name")
def change_last_name(new_last_name: str, token: str = Header(...)):
    """
    Update a user's last name
    """
    headers_request = create_header_token(token)
    new_last_name = {"new_last_name": new_last_name}
    url = USERS_URL + "/users/last_name"

    response = requests.put(
        url, params=new_last_name, headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)


# Route to update a user's location
@router.put("/users/location")
def change_location(new_location: str, token: str = Header(...)):
    """
    Update a user's location
    """
    headers_request = create_header_token(token)
    new_location = {"new_location": new_location}
    url = USERS_URL + "/users/location"

    response = requests.put(
        url, params=new_location, headers=headers_request, timeout=TIMEOUT
    )
    return generate_response(response)
