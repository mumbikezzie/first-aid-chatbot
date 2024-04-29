from datetime import datetime
from pydantic import BaseModel, UUID4
from typing import Any, Optional

class MessageCreate(BaseModel):
    text: str