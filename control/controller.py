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
from control.posts import favorites
from control.posts import likes
from control.posts import notifications
from control.posts import reposts
from control.posts import trending_topics

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
