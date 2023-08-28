#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from pydantic import BaseModel


class CountryBase(BaseModel):
    name: str


class CountryCreate(CountryBase):
    pass


class Country(CountryBase):
    id: int
    region_id: int

    class Config:
        orm_mode = True


class ChapterBase(BaseModel):
    number: int
    text: str


class ChapterCreate(ChapterBase):
    pass


class Chapter(ChapterBase):
    id: int
    country: Country

    class Config:
        orm_mode = True
