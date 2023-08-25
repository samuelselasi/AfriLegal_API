#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from typing import List, Union, Optional
from pydantic import BaseModel

#from ..user.schemas import User, UserBase
from api.routers.user.schemas import User, UserBase


class Auth(UserBase):
    password: str


class AuthResponse(BaseModel):
    access_token: str
    refresh_token: str
    user: User

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: Optional[str]
    refresh_token: Optional[str]
