# controler.py

"""
This is the gateway to the application. It is the only file that should be
"""


# Para permitir pegarle a la API desde localhost:
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Para permitir pegarle a la API desde localhost: (PREGUNTAR)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Route to handle user registration
@app.post("/register/")
def register():
    """
    Register a new user
    """


# Aca se llamaria a el endpoint de la API de usuarios
