# env.py
"""
Module dedicated for environment variables
"""
import os

USERS_URL = os.environ.get("USERS_URL")
if USERS_URL is None:
    print("You forgot to set USERS_URL!")

SNAPMSG_URL = os.environ.get("SNAPMSG_URL")
if SNAPMSG_URL is None:
    print("You forgot to set URL_SNAPMSG!")

ADMINS_URL = os.environ.get("ADMINS_URL")
if ADMINS_URL is None:
    print("You forgot to set ADMINS_URL!")

METRICS_URL = os.environ.get("METRICS_URL")
if METRICS_URL is None:
    print("You forgot to set METRICS_URL!")
