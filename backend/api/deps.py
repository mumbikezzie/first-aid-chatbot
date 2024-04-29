from typing import Generator
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from settings.config import settings
from jose import JWTError, jwt
from db.session import SessionLocal
from crud.user_crud import user_crud
from models.user import Users
# from datetime import datetime

from requests import Session

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/user/login/access-token"
)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# get current user middleware -> to be injected to every route that needs to be guarded
async def get_current_user(db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)):
    credential_exception = HTTPException(
        status_code=401,
        detail="Invalid Credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

        user_id: str = payload.get("sub")
        if user_id is None:
            raise credential_exception

        # # Check token expiration
        # exp = payload.get("exp")
        # if exp is None or exp < datetime.utcnow():
        #     raise HTTPException(status_code=401, detail="Token has expired")

    except JWTError as e:
        raise HTTPException(status_code=401, detail=f'{e}')

    # TODO: get the user by the id function from crud
    user = user_crud.get(db, user_id)

    if user is None:
        raise credential_exception
    return user


def get_current_active_user(
        current_user: Users = Depends(get_current_user),
) -> Users:
    if not user_crud.is_active(Users, user=current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
