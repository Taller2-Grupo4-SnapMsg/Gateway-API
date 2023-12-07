# trending_topics.py
"""
Module for the endpoints of the trending topics
"""
from urllib.parse import quote
import requests
from fastapi import APIRouter, Header, Query
from control.utils import generate_response
from control.utils import create_header_token
from control.env import SNAPMSG_URL

router = APIRouter(tags=["Trending Topics"])
origins = ["*"]

TIMEOUT = 20


@router.get("/trending_topics")
def get_trending_topics(
    offset=Query(0, title="offset", description="offset for pagination"),
    amount=Query(10, title="ammount", description="max ammount of users to return"),
    days=Query(
        7, title="days", description="to take into account the posts of the last x days"
    ),
    token: str = Header(...),
):
    """
    Get trending topics
    """
    headers_request = create_header_token(token)
    params = {
        "offset": int(offset),
        "ammount": int(amount),
        "days": int(days),
    }
    # pylint: disable=line-too-long
    url = f"{SNAPMSG_URL}/trending_topics?offset={params['offset']}&ammount={params['ammount']}&days={params['days']}"

    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)


@router.get("/posts/trending_topic/{hashtag}")
def get_posts_on_a_trending_topic(
    hashtag: str,
    offset=Query(0, title="offset", description="offset for pagination"),
    amount=Query(10, title="ammount", description="max ammount of users to return"),
    token: str = Header(...),
):
    """
    Get posts on a trending topic
    """
    headers_request = create_header_token(token)
    params = {
        "offset": int(offset),
        "ammount": int(amount),
    }
    # pylint: disable=line-too-long
    url = f"{SNAPMSG_URL}/posts/trending_topic/{quote(hashtag)}?offset={params['offset']}&ammount={params['ammount']}"

    response = requests.get(url, headers=headers_request, timeout=TIMEOUT)

    return generate_response(response)
