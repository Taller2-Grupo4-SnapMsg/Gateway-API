# models.py
"""
This module is for the Pydantic models.
"""
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

# Define a Pydantic model for the request body
class PostCreateRequest(BaseModel):
    """
    This class is a Pydantic model for the request body.
    """

    user_id: int
    content: str
    image: str


class UserResponse(BaseModel):
    """
    This class is a Pydantic model for the User part of the response body.
    This way, with the post in the response, the front already gets the information from
    the corresponding User
    """

    username: str
    name: str
    last_name: str
    avatar: str


class PostResponse(BaseModel):
    """
    This class is a Pydantic model for the response body.
    """

    id: int
    user: UserResponse
    posted_at: str
    content: str
    image: str



class LikeCreateRequest(BaseModel):
    """
    This class is a Pydantic model for the request body.
    """

    post_id: int

