# models.py
"""
This module is for the Pydantic models.
"""
from typing import List, Dict
from pydantic import BaseModel


class UserRegistration(BaseModel):
    """
    This class is a Pydantic model for the request body.
    """

    password: str
    email: str
    name: str
    last_name: str
    username: str
    date_of_birth: str


class UserLogIn(BaseModel):
    """
    This class is a Pydantic model for the request body.
    """

    email: str
    password: str


class PostCreateRequest(BaseModel):
    """
    This class is a Pydantic model for the request body.
    """

    content: str
    image: str
    hashtags: List[str]
    mentions: List[str]


class NotificationRequest(BaseModel):
    """
    This class is a Pydantic model for the request body.
    """

    user_emails_that_receive: List[str]
    title: str
    body: str
    data: Dict[str, str]
