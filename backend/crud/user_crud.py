from typing import Any, Optional, List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from utils.security import get_password_hash

from fastapi_pagination import paginate
from crud.base import CRUDBase
from schemas.user import UserCreate, UserUpdate, UserOut
from models.user import Users


class CRUDUser(CRUDBase[UserCreate, UserUpdate, UserOut]):

    @staticmethod
    def get_by_email(self, db: Session, *, email: str) -> Optional[UserOut]:
        return db.query(Users).filter(Users.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> Users:
        # check whether the email exists
        user = db.query(Users).filter(Users.email == obj_in.email).first()

        if user:
            raise HTTPException(status_code=400, detail="User with such an email already exists")

        usr_obj = Users(
            first_name=obj_in.first_name,
            last_name=obj_in.last_name,
            email=obj_in.email,
            password=obj_in.password,
            is_active=obj_in.is_active,
        )

        hashed_password = get_password_hash(usr_obj.password)

        usr_obj.password = hashed_password

        # save the record
        db.add(usr_obj)
        db.commit()
        db.refresh(usr_obj)
        return usr_obj

    @staticmethod
    def is_active(self, user: Users) -> bool:
        return user.is_active


user_crud = CRUDUser(Users)
