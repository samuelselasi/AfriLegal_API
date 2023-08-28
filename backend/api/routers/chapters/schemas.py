#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from pydantic import BaseModel


class CountryBase(BaseModel):
    """Class that defines public instance attributes"""

    name: str


class CountryCreate(CountryBase):
    """Class that passes instance attributes"""

    pass


class Country(CountryBase):
    """Class that defines instance attributes"""

    id: int
    region_id: int

    class Config:
        """Class that configures ORM mode"""

        orm_mode = True


class ChapterBase(BaseModel):
    """Class that defines instance attributes"""

    number: int
    text: str


class ChapterCreate(ChapterBase):
    """Class that passes instance attributes"""

    pass


class Chapter(ChapterBase):
    """Class that defines instance attributes"""

    id: int
    country: Country

    class Config:
        """Class that configures ORM mode"""

        orm_mode = True
