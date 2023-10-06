# posts.py
"""
This is the users' followers micro-service represented in the gateway.
"""
from urllib.parse import quote
import requests
from fastapi import APIRouter, Header
from control.utils import create_post_payload
from control.utils import generate_response
from control.utils import create_header_token
from control.models import PostCreateRequest
from control.env import POSTS_URL

router = APIRouter()
origins = ["*"]

TIMEOUT = 40

# A probar
@router.post("/post")
def create_post(post_data: PostCreateRequest,  token: str = Header(...)):
    """
    Create new post
    """
    payload = create_post_payload(post_data)
    headers_request = create_header_token(token)
    url = POSTS_URL + "/posts"
    # call to posts's API
    response = requests.post(
        url, json=payload, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)

# A probar
@router.get("/posts")
def get_posts(token: str = Header(...)):
    """
    Gets all posts ever created. Use with caution!
    """
    headers_request = create_header_token(token)
    url = POSTS_URL + "/posts"
    # call to posts's API
    response = requests.get(
        url, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)

# A probar
@router.get("/post/{id}")
def get_posts(token: str = Header(...)):
    """
    Gets post with that ID.
    """
    headers_request = create_header_token(token)
    post_id = {"id": id}
    url = f"{POSTS_URL}/posts/{quote(post_id['id'])}"
    response = requests.get(
        url, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)

# A probar
@router.get("/posts/user/")
def get_posts_by_user(token: str = Header(...)):
    """
    Gets all posts made by that user
    """
    headers_request = create_header_token(token)
    url = f"{POSTS_URL}/posts/user"
    response = requests.get(
        url, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)

# A probar
@router.get("/posts/user/amount/{x}")
async def api_get_x_newest_posts_by_user(x: int, token: str = Header(...)):
    """
    Gets x amount of newest posts made by that user (the owner of the token)
    """
    headers_request = create_header_token(token)
    amount = {"x": x}
    url = f"{POSTS_URL}/posts/user/amount/{quote(amount['x'])}"
    response = requests.get(
        url, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)

# A probar
@router.get("/posts/amount/{x}")
async def api_get_x_newest_posts(x: int, token: str = Header(...)):
    """
    Gets x amount of newest posts made in general
    """
    headers_request = create_header_token(token)
    amount = {"x": x}
    url = f"{POSTS_URL}/posts/user/amount/{quote(amount['x'])}"
    response = requests.get(
        url, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)

# A probar
@router.delete("/post/{id}")
async def api_delete_post(id: int, token: str = Header(...)):
    """
    Deletes post with that id
    """
    headers_request = create_header_token(token)
    post_id = {"id": id}
    url = f"{POSTS_URL}/post/{quote(post_id['id'])}"
    response = requests.delete(
        url, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)