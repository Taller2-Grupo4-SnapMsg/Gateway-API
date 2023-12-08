# block.py
"""
This module is the gateway to the metrics' block functions.
"""

# pylint: disable=R0801
# We disable the similar code becase we have no time for refactor,
# we have to deliver the project at 17:00 lmao

from fastapi import APIRouter, Header
import requests
from control.utils import (
    generate_response,
    create_header_token,
    TIMEOUT,
)
from control.env import METRICS_URL

router = APIRouter(tags=["metrics-block"])
origins = ["*"]


@router.get("/block")
def get_blocks(timestamp_end: str, token: str = Header(...)):
    """
    Get the number of blocks in a given time range
    """
    headers_request = create_header_token(token)
    params = {"timestamp_end": timestamp_end}
    response = requests.get(
        METRICS_URL + "/block",
        params=params,
        headers=headers_request,
        timeout=TIMEOUT,
    )
    return generate_response(response)


@router.get("/block/blocked_now")
def get_blocked_now(token: str = Header(...)):
    """
    Get the number of blocks in a given time range
    """
    headers_request = create_header_token(token)
    response = requests.get(
        METRICS_URL + "/block/blocked_now",
        headers=headers_request,
        timeout=TIMEOUT,
    )
    return generate_response(response)
