from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Any

from .user import UserOut


class LoginCreate(BaseModel):
    username: str
    password: str

class LoginWithToken(BaseModel):
    user: UserOut
    access_token: str
    token_type: str
    expires_in: int