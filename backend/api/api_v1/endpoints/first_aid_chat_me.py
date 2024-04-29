from nltk.chat.util import Chat, reflections
from utils.pairs import pairs, my_data

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List
from fastapi_pagination import Page, paginate
from schemas.aid import MessageCreate

from api import deps
from models.user import Users
from api.deps import get_db
from schemas.user import UserCreate, UserOut, UserUpdate
from crud.user_crud import user_crud

router = APIRouter()

@router.post('/chat-me')
async def chat_with_first_aid(message:  MessageCreate):

    chat = Chat(my_data, reflections)
    response = chat.respond(message.text)

    print("Response", response)

    if response == None:
        return {"status": "ERROR", "message": "Sorry,I don't understand that."}
    else:

        formatted_response = {
            "sender_message": message.text,
            "reply_message": response,
        },

        return {"status": "SUCCESS", "message": formatted_response}
