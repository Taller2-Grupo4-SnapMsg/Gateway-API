# controler.py
"""
This is the gateway to the application. It is the only file that should be
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from control.users import users

app = FastAPI()
origins = ["*"]

app.include_router(users.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Despues cuando se cree snapmsg.py:
URL_SNAPMSG = os.environ.get("URL_SNAPMSG")
if URL_SNAPMSG is None:
    print("You forgot to set URL_SNAPMSG!")
