from typing import Union
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from api.api_v1.api import api_router
from settings.config import settings

app = FastAPI(
    title="First Aid Chatbot Backend",
    description="A platform to manage first aid chat operations",
    redoc_url="/developer/redoc",
    docs_url="/developer/docs",
    contact={
        "name": "Keziah Mumbi",
        "email": "developer@example.com"
    }
)

# middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR, responses={
    200: {'description': 'Ok'},
    201: {'description': 'Created'},
    202: {'description': 'Accepted'},
    400: {"description": "Bad Request"},
    401: {"description": "Unauthorized"},
    403: {"description": "Forbidden"},
    404: {"description": "Not found"},
    405: {"description": "Method not allowed"},
    408: {"description": "Request timeout"},
    409: {"description": "Conflict"},
    422: {"description": "Unprocessable entity"},
    500: {"description": "Internal server error"},
    502: {"description": "Bad Gateway"},
    503: {"description": "Service Unavailable"},
    504: {"description": "Gateway Timeout"},
})

# from fastapi_pagination import add_pagination
# add_pagination(app)