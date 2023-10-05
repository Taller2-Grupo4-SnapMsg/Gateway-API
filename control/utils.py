# utils.py
"""
Module for utility functions
"""

from fastapi import HTTPException


def generate_response(response):
    """
    Generate a response from a given request return value
    """
    if response.status_code == 200:
        data = response.json()
        return data

    raise HTTPException(
        status_code=response.status_code, detail=response.json().get("detail")
    )


def create_header_token(token):
    """
    Create a header with a token
    """
    return {
        "accept": "application/json",
        "Content-Type": "application/json",
        "token": token,
    }
