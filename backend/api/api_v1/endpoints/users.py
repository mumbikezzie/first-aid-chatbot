from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Any, List
from fastapi_pagination import Page, paginate

from api import deps
from models.user import Users
from api.deps import get_db
from schemas.user import UserCreate, UserOut, UserUpdate
from crud.user_crud import user_crud


# instance the router
router = APIRouter()


@router.get("/{id}",
            response_model=UserOut,
            response_description="Returns a single internal user information",
            status_code=200,
            )
async def get_single_user(id: str, db: Session = Depends(get_db),
                          current_user: Users = Depends(deps.get_current_user)):
    user = user_crud.get(db=db, id=id)

    if user is None:
        raise HTTPException(
            status_code=404, detail=f"Internal User with id {id} does not exist")

    return user


@router.get("",
            response_model=List[UserOut],
            response_description="Returns a list of internal users based on the specified query",
            status_code=200
            )
async def get_all_users(db: Session = Depends(get_db),
                        current_user: Users = Depends(deps.get_current_user)):
    try:
        users = user_crud.get_multi(db=db)
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{e}')


@router.post("",
             response_model=UserOut,
             response_description="Returns a new internal user object that has been created",
             status_code=201
             )
async def create_new_user(user_in: UserCreate, db: Session = Depends(get_db),
                          ):
    user = user_crud.create(db=db, obj_in=user_in)

    return user


@router.put("/{id}",
            response_model=UserOut,
            response_description="Returns new information of an existing internal user",
            status_code=200
            )
async def update_existing_user(id: str, user_payload: UserUpdate, db: Session = Depends(get_db),
                               current_user: Users = Depends(deps.get_current_user)):
    user = user_crud.get(db=db, id=id)

    if user is None:
        raise HTTPException(
            status_code=404, detail=f"Internal user with id {id} does not exist")

    updated_user = user_crud.update(db=db, db_obj=user, obj_in=user_payload)

    return updated_user


@router.delete("/{id}",
               response_model=Page[UserOut],
               response_description="Success of Failure after removal of an existing internal user",
               )
async def remove_existing_user(id: str, db: Session = Depends(get_db),
                               current_user: Users = Depends(deps.get_current_user)):
    try:
        user = user_crud.get(db=db, id=id)

        if user is None:
            raise HTTPException(status_code=404, detail=f"Internal user with id {id} does not exist")

        user_crud.remove(db=db, id=id)
        new_users = user_crud.get_multi(db=db)

        return new_users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    # finally:
    #     db.close()
