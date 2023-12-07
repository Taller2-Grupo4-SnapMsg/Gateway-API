# users_admin.py
"""
Module for the endpoints of the users' API that are only available for admins
"""

from urllib.parse import quote
import requests
from fastapi import APIRouter, Header, Query, HTTPException, status
from control.models import UserLogIn
from control.utils import generate_response
from control.utils import create_header_token
from control.utils import create_header_no_token
from control.env import USERS_URL
from control.env import ADMINS_URL
from control.env import SNAPMSG_URL
from control.env import METRICS_URL

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


@router.get("/users/admin/image")
def get_image_from_path(firebase_path: str, token: str = Header(...)):
    """
    Translates a firebase_path into a valid url image that expires in 5 minutes.
    """
    headers_request = create_header_token(token)
    url = USERS_URL + "/users/admin/image"
    params = {"firebase_path": firebase_path}
    response = requests.get(
        url, params=params, headers=headers_request, timeout=TIMEOUT
    )
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


@router.get("/service_status")
def get_service_status(service: str = Query(...)):
    """
    Get the status of the service
    """
    if service == "users":
        url = USERS_URL
    elif service == "admins":
        url = ADMINS_URL + "/admin"
    elif service == "snapmsg":
        url = SNAPMSG_URL + "/admin"
    elif service == "metrics":
        url = METRICS_URL + "/admin"
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found: " + service,
        )

    url += "/health"
    response = requests.get(url, timeout=TIMEOUT)

    return generate_response(response)


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
