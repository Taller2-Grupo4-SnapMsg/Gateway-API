# controler.py
"""
This is the gateway to the application. It is the only file that should be
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from control.users import (
    users,
    users_put,
    users_admin,
    followers,
)
from control.posts import (
    posts,
    favorites,
    likes,
    reposts,
    notifications,
    trending_topics,
)
from control.metrics import (
    block,
    geo_zones,
    login,
    registration,
)

app = FastAPI()
origins = ["*"]

app.include_router(users.router)
app.include_router(users_put.router)
app.include_router(users_admin.router)
app.include_router(followers.router)
app.include_router(posts.router)
app.include_router(favorites.router)
app.include_router(likes.router)
app.include_router(notifications.router)
app.include_router(reposts.router)
app.include_router(trending_topics.router)
app.include_router(block.router)
app.include_router(geo_zones.router)
app.include_router(login.router)
app.include_router(registration.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
