# utils.py
"""
Module for utility functions
"""

from fastapi import HTTPException, status


def generate_response(response):
    """
    Generate a response from a given request return value
    """
    if response.status_code == status.HTTP_200_OK:
        data = response.json()
        return data
    if response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Sorry, something went wrong, try again later",
        )
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


def create_header_biometric_token(biometric_token):
    """
    Create a header with a token
    """
    return {
        "accept": "application/json",
        "Content-Type": "application/json",
        "biometric-token": biometric_token,
    }


def create_header_biometric_token_and_user_token(token, biometric_token):
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


def create_post_content_payload(post):
    """
    Create a payload for post content
    """
    return {
        "content": post.content,
        "image": post.image,
        "hashtags": post.hashtags,
        "mentions": post.mentions,
    }


def create_notification_payload(notification):
    """
    Create a payload for notification
    """
    return {
        "user_emails_that_receive": notification.user_emails_that_receive,
        "title": notification.title,
        "body": notification.body,
        "data": notification.data,
    }


def create_header_no_token():
    """
    Create a header with no token
    """
    return {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
