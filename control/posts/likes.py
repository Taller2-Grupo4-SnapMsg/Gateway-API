# likes.py
"""
This is the users' followers micro-service represented in the gateway.
"""
from urllib.parse import quote
import requests
from fastapi import APIRouter, Header
from control.utils import generate_response
from control.utils import create_header_token

router = APIRouter()
origins = ["*"]

TIMEOUT = 20

# # Route to create a follow:
# @router.post("/likes")
# def create_like(post_id: int, token: str = Header(...)):
#     """
#     Create a follow
#     """
#     headers_request = create_header_token(token)
#     post_id = {"post_id": post_id}
#     url = f"{POSTS_URL}/likes/{quote(post_id['post_id'])}"
#     # call to user's API
#     response = requests.post(
#         url, params=email, headers=headers_request, timeout=TIMEOUT
#     )

#     return generate_response(response)

# @router.post("/likes", tags=["Likes"])
# async def api_create_like(post_id: int, token: str = Header(...)):
#     """
#     Creates a new like

#     Args:
#         like (Like): The like to create.

#     Returns:
#         Like: The like that was created.

#     Raises:
#         -
#     """
#     headers = {
#         "Content-Type": "application/json;charset=utf-8",
#         "accept": "application/json",
#         "token": token,
#     }

#     async with httpx.AsyncClient() as client:
#         try:
#             response = await client.get(
#                 "https://loginback-lg51.onrender.com/user", headers=headers
#             )
#             print(f"RESPONSE: {response}")
#             if response.status_code == 200:
#                 user = response.json()
#                 create_like(post_id, user.get("id"))
#                 return {"message": "Like created successfully"}
#             raise HTTPException(status_code=400, detail={"Unknown error"})
#         except httpx.HTTPError as error:
#             raise HTTPException(status_code=400, detail={str(error)}) from error