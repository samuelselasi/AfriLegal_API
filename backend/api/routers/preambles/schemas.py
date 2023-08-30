#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from typing import List
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


class RegionBase(BaseModel):
    name: str


class RegionCreate(RegionBase):
    name: str


class Region(RegionBase):
    id: int
    is_active: bool
    countries: List[Country] = []

    class Config:
        orm_mode = True


class PreambleBase(BaseModel):
    text: str


class PreambleCreate(PreambleBase):
    pass


class Preamble(PreambleBase):
    id: int
    country: Country

    class Config:
        orm_mode = True
