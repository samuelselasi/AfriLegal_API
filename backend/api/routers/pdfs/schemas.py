#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from pydantic import BaseModel


class PDFBase(BaseModel):
    """Class that defines instance attributes"""

    title: str


class PDFCreate(PDFBase):
    """Class that defines instance attributes"""

    content: bytes


class PDF(PDFBase):
    """Class that defines instance attributes"""

    id: int

    class Config:
        """Class that configures ORM mode"""

        orm_mode = True
