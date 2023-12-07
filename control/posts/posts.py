# pylint: disable=R0801
# posts.py
"""
This is the posts micro service represented in the gateway.
"""
from urllib.parse import quote
import requests
from fastapi import APIRouter, Header, Query
from control.models import PostCreateRequest
from control.utils import generate_response
from control.utils import create_header_token
from control.utils import create_post_content_payload
from control.env import SNAPMSG_URL

router = APIRouter(tags=["posts"])
origins = ["*"]

TIMEOUT = 20


@router.post("/posts")
def create_post(post: PostCreateRequest, token: str = Header(...)):
    """
    Create a post
    """
    payload = create_post_content_payload(post)
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/posts"

    response = requests.post(
        url, json=payload, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)


@router.get(
    "/posts/profile/{user_visited_email}/oldest_date/{oldest_date_str}"
    "/amount/{amount}/only_reposts/",
)
def get_posts_and_reposts_from_user_visited(
    user_visited_email: str,
    oldest_date_str: str,
    amount: int,
    only_reposts: bool,
    token: str = Header(...),
):
    """
    Get posts and reposts from a user
    """
    headers_request = create_header_token(token)
    # pylint: disable=line-too-long
    url = f"{SNAPMSG_URL}/posts/profile/{user_visited_email}/oldest_date/{oldest_date_str}/amount/{amount}/only_reposts/"
    params = {"only_reposts": only_reposts}
    response = requests.get(
        url, headers=headers_request, params=params, timeout=TIMEOUT
    )
    return generate_response(response)


@router.get("/posts/{post_id}")
def get_post_by_id(post_id: int, token: str = Header(...)):
    """
    Get a post by id
    """
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/posts/{post_id}"

    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


@router.get("/posts/profile/{user_visited_email}")
def get_amount_posts_from_user_visited(
    user_visited_email: str,
    token: str = Header(...),
):
    """
    Get amount of posts from a user
    """
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/posts/profile/{user_visited_email}"

    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


@router.get("/posts/feed/oldest_date/{oldest_date_str}/amount/{amount}")
def get_feed(oldest_date_str: str, amount: int, token: str = Header(...)):
    """
    Get a user's feed
    """
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/posts/feed/oldest_date/{oldest_date_str}/amount/{amount}"

    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


@router.get("/posts/statistics/from_date/{from_date_str}/to_date/{to_date_str}")
def get_statistics(from_date_str: str, to_date_str: str, token: str = Header(...)):
    """
    Get statistics from a user
    """
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/posts/statistics/from_date/{from_date_str}/to_date/{to_date_str}"

    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


@router.get("/posts/search/hashtags/{hashtags}")
def get_posts_by_hashtags(
    hashtags: str,
    offset=Query(0, title="offset", description="offset for pagination"),
    amount=Query(10, title="ammount", description="max ammount of users to return"),
    token: str = Header(...),
):
    """
    Get posts by hashtags
    """
    headers_request = create_header_token(token)
    params = {
        "hashtags": hashtags,
        "offset": int(offset),
        "ammount": int(amount),
    }
    # pylint: disable=line-too-long
    url = f"{SNAPMSG_URL}/posts/search/hashtags/{quote(params['hashtags'])}?offset={params['offset']}&ammount={params['ammount']}"

    response = requests.get(
        url, params=params, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)


@router.get("/posts/search/text/{text}")
def get_posts_by_text(
    text: str,
    offset=Query(0, title="offset", description="offset for pagination"),
    amount=Query(10, title="ammount", description="max ammount of users to return"),
    token: str = Header(...),
):
    """
    Get posts by text
    """
    headers_request = create_header_token(token)
    params = {
        "text": text,
        "offset": int(offset),
        "ammount": int(amount),
    }
    # pylint: disable=line-too-long
    url = f"{SNAPMSG_URL}/posts/search/text/{quote(params['text'])}?offset={params['offset']}&ammount={params['ammount']}"

    response = requests.get(
        url, params=params, headers=headers_request, timeout=TIMEOUT
    )

    return generate_response(response)


@router.put("/posts/{post_id}")
def update_post(post_id: int, post_data: PostCreateRequest, token: str = Header(...)):
    """
    Update a post
    """
    payload = create_post_content_payload(post_data)
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/posts/{post_id}"

    response = requests.put(url, json=payload, headers=headers_request, timeout=TIMEOUT)
    print(response)
    return generate_response(response)


@router.delete("/posts/{post_id}")
def delete_post(post_id: int, token: str = Header(...)):
    """
    Delete a post
    """
    headers_request = create_header_token(token)
    url = f"{SNAPMSG_URL}/posts/{post_id}"

    response = requests.delete(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)
