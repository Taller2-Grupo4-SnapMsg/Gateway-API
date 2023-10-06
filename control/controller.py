# controler.py
"""
This is the gateway to the application. It is the only file that should be
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from control.users import users
from control.users import followers
from control.users import users_put
from control.users import users_admin
from control.posts import posts
from control.posts import likes

app = FastAPI()
origins = ["*"]

app.include_router(users.router)
app.include_router(users_put.router)
app.include_router(users_admin.router)
app.include_router(followers.router)
app.include_router(posts.router)
app.include_router(likes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
