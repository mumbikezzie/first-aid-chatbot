from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Any

from schemas.authentication import LoginWithToken
from api import deps
from models.user import Users
from utils.security import verify_password, create_access_token
from settings.config import settings
from schemas.user import UserOut

# instanciate the router
router = APIRouter()


@router.post("/login/access-token", response_model=LoginWithToken)
async def login(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    # check whether the user exists
    user = db.query(Users).filter(
        Users.email == form_data.username).first()

    if not user:
        raise HTTPException(
            status_code=401, detail="No account matches the email provided")

    # compare the two passwords
    if not verify_password(form_data.password, hashed_password=user.password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    # check whether the account is active
    if not user.is_active:
        raise HTTPException(
            status_code=401, detail="User Account has been deactivated! Contact Admin.")

    # generate a JWT Token
    access_token_expires = timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    print("ACCESS", access_token_expires)
    # access_token_expires_in_milliseconds = settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    # Calculate the expiration time in seconds
    expires_in_seconds = access_token_expires.total_seconds()
    print("AACCESS", expires_in_seconds)
    access_token = create_access_token(user.id, access_token_expires)
    # return the LoginWithToken response
    return {
        "access_token": access_token,
        "token_type": "Bearer",
        "expires_in": expires_in_seconds,
        "user": user
    }


@router.get("/me", summary="read current logged in user", response_model=UserOut)
def read_user_me(
        db: Session = Depends(deps.get_db),
        current_user: Users = Depends(deps.get_current_user),
) -> Any:
    """
    Get current user.
    """
    return current_user
