from datetime import datetime
from pydantic import BaseModel, UUID4
from typing import Any, Optional

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    is_active: bool

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class UserOut(UserBase):
    id: Any
    created_ts: Optional[datetime]
    updated_ts: Optional[datetime]