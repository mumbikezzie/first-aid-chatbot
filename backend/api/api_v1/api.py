from fastapi import APIRouter

from api.api_v1.endpoints import authentication, users, first_aid_chat_me

api_router = APIRouter()

api_router.include_router(authentication.router, prefix="/user", tags=["USER AUTHENTICATION"])
api_router.include_router(users.router, prefix="/users", tags=["USER MANAGEMENT"])
api_router.include_router(first_aid_chat_me.router, prefix='/first-aid', tags=["FIRST AID OPERATIONS"])
