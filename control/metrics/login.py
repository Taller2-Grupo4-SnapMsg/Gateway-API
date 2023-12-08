# login.py
"""
This module is the gateway to the metrics' login functions.
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

router = APIRouter(tags=["metrics-login"])
origins = ["*"]


@router.get("/metrics_login")
def get_login(
    entity: str,
    successful: bool,
    timestamp_begin: str,
    timestamp_end: str,
    token: str = Header(...),
):
    """
    Get amount of logins from the entity

    If entity is "email", only the amount of logins
    made from email and password will be returned

    If entity is "federated", only the amount of logins
    made from everything that is not email and password will be returned
        (Google, Facebook and everything else)

    If entity is "all", no distinction will be made, the amount of all logins will be returned
    """
    headers_request = create_header_token(token)
    params = {
        "entity": entity,
        "successful": successful,
        "timestamp_begin": timestamp_begin,
        "timestamp_end": timestamp_end,
    }
    response = requests.get(
        METRICS_URL + "/login",
        params=params,
        headers=headers_request,
        timeout=TIMEOUT,
    )
    return generate_response(response)


@router.get("/login/average_time")
def get_login_average_time(
    timestamp_begin: str, timestamp_end: str, token: str = Header(...)
):
    """
    Get the average time it takes to log in
    """
    headers_request = create_header_token(token)
    params = {"timestamp_begin": timestamp_begin, "timestamp_end": timestamp_end}
    response = requests.get(
        METRICS_URL + "/login/average_time",
        params=params,
        headers=headers_request,
        timeout=TIMEOUT,
    )
    return generate_response(response)
