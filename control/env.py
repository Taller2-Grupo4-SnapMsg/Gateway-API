# env.py
"""
Module dedicated for environment variables
"""
import os

USERS_URL = os.environ.get("USERS_URL")
if USERS_URL is None:
    print("You forgot to set USERS_URL!")

# Despues cuando se cree snapmsg.py:
POSTS_URL = os.environ.get("POSTS_URL")
if POSTS_URL is None:
    print("You forgot to set POSTS_URL!")
