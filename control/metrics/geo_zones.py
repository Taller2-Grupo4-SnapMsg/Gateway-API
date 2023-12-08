# geo_zones.py
"""
This module is the gateway to the metrics' geo_zones functions.
"""

from fastapi import APIRouter, Header, Query
import requests
from control.utils import (
    generate_response,
    create_header_token,
    TIMEOUT,
)
from control.env import METRICS_URL

router = APIRouter(tags=["metrics-geo_zones"])
origins = ["*"]


@router.get("/geozones/amount")
def get_geozones_amount(
    timestamp_end: str,
    amount: int = Query(None, description="amount"),
    token: str = Header(...),
):
    """
    Get the geo zones with amount of users in a given range
    (amount is optional, if given, for example "2" will return all the zones
    that have 2 users in them)
    """
    headers_request = create_header_token(token)
    params = {"timestamp_end": timestamp_end, "amount": amount}
    response = requests.get(
        METRICS_URL + "/geozones/amount",
        params=params,
        headers=headers_request,
        timeout=TIMEOUT,
    )
    return generate_response(response)
