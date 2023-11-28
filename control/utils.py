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
        status_code=response.status_code, detail=response.json().get("message")
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


def create_header_tokens(token, biometric_token):
    """
    Create a header with a token
    """
    return {
        "accept": "application/json",
        "Content-Type": "application/json",
        "token": token,
        "biometric-token": biometric_token,
    }


def create_user_registration_payload(user_data):
    """
    Create a payload for user registration
    """
    return {
        "password": user_data.password,
        "email": user_data.email,
        "name": user_data.name,
        "last_name": user_data.last_name,
        "username": user_data.username,
        "date_of_birth": user_data.date_of_birth,
    }


def create_header_no_token():
    """
    Create a header with no token
    """
    return {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
