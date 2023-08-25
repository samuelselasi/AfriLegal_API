#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: Optional[str]
    user_type_id: int
    status: Optional[bool]


class UserUpdate(BaseModel):
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]


class ResetPassword(BaseModel):
    password: str
    code: Optional[str]


class ChangePassword(BaseModel):
    email: str
    password: str


class User(UserBase):
    id: int
    user_type_id: int

    class Config:
        orm_mode = True
