# registration.py
"""
This module is the gateway to the metrics' registration functions.
"""

from fastapi import APIRouter, Header
import requests
from control.utils import (
    generate_response,
    create_header_token,
    TIMEOUT,
)
from control.env import METRICS_URL

router = APIRouter(tags=["metrics-registration"])
origins = ["*"]


@router.get("/registration/amount")
def get_registration(
    timestamp_begin: str, timestamp_end: str, token: str = Header(...)
):
    """
    Get the amount of registrations in a given time range
    """
    headers_request = create_header_token(token)
    params = {"timestamp_begin": timestamp_begin, "timestamp_end": timestamp_end}
    response = requests.get(
        METRICS_URL + "/registration/amount",
        params=params,
        headers=headers_request,
        timeout=TIMEOUT,
    )

    return generate_response(response)


@router.get("/registration/average_time")
def get_registration_average_time(
    timestamp_begin: str, timestamp_end: str, token: str = Header(...)
):
    """
    Get the average time it takes to register
    """
    headers_request = create_header_token(token)
    params = {"timestamp_begin": timestamp_begin, "timestamp_end": timestamp_end}
    response = requests.get(
        METRICS_URL + "/registration/average_time",
        params=params,
        headers=headers_request,
        timeout=TIMEOUT,
    )

    return generate_response(response)
