# env.py
"""
Module dedicated for environment variables
"""
import os

USERS_URL = os.environ.get("USERS_URL")
if USERS_URL is None:
    print("You forgot to set USERS_URL!")

# Despues cuando se cree snapmsg.py:
URL_SNAPMSG = os.environ.get("URL_SNAPMSG")
if URL_SNAPMSG is None:
    print("You forgot to set URL_SNAPMSG!")
