#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from typing import List, Union
from pydantic import BaseModel


class ItemBase(BaseModel):
    """Class that defines public instance attributes"""

    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    """Class that passes public instance attributes"""

    pass


class Item(ItemBase):
    """Class that defines public instance attributes"""

    id: int
    owner_id: int

    class Config:
        """Class that configures ORM mode"""

        orm_mode = True


class UserBase(BaseModel):
    """Class that defines public instance attributes"""

    email: str


class UserCreate(UserBase):
    """Class that defines public instance attributes"""

    password: str


class User(UserBase):
    """Class that defines public instance attributes"""

    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        """Class that configures ORM mode"""

        orm_mode = True


class CountryBase(BaseModel):
    """Class that defines public instance attributes"""

    name: str


class CountryCreate(CountryBase):
    """Class that passes public instance attributes"""

    pass


class Country(CountryBase):
    """Class that defines public instance attributes"""

    id: int
    region_id: int

    class Config:
        """Class that configures ORM mode"""

        orm_mode = True


class RegionBase(BaseModel):
    """Class that defines public instance attributes"""

    name: str


class RegionCreate(RegionBase):
    """Class that defines public instance attributes"""

    name: str


class Region(RegionBase):
    """Class that defines public instance attributes"""

    id: int
    is_active: bool
    countries: List[Country] = []

    class Config:
        """Class that configures ORM mode"""

        orm_mode = True


class PreambleBase(BaseModel):
    """Class that defines public instance attributes"""

    text: str


class PreambleCreate(PreambleBase):
    """Class that passes public instance attributes"""

    pass


class Preamble(PreambleBase):
    """Class that defines public instance attributes"""

    id: int
    country: Country

    class Config:
        """Class that configures ORM mode"""

        orm_mode = True


class ChapterBase(BaseModel):
    """Class that defines public instance attributes"""

    number: int
    text: str


class ChapterCreate(ChapterBase):
    """Class that passes public instance attributes"""

    pass


class Chapter(ChapterBase):
    """Class that defines public instance attributes"""

    id: int
    country: Country

    class Config:
        """Class that configures ORM mode"""

        orm_mode = True


class ArticleBase(BaseModel):
    """Class that defines public instance attributes"""

    number: int
    title: str
    text: str


class ArticleCreate(ArticleBase):
    """Class that passes public instance attributes"""

    pass


class Article(ArticleBase):
    """Class that defines public instance attributes"""

    id: int
    country: Country
    chapter: Chapter

    class Config:
        """Class that configures ORM mode"""

        orm_mode = True


class SectionBase(BaseModel):
    """Class that defines public instance attributes"""

    number: int
    text: str


class SectionCreate(SectionBase):
    """Class that passes public instance attributes"""

    pass


class Section(SectionBase):
    """Class that defines public instance attributes"""

    id: int
    country: Country
    chapter: Chapter
    article: Article

    class Config:
        """Class that configures ORM mode"""

        orm_mode = True


class SubsectionBase(BaseModel):
    """Class that defines public instance attributes"""

    sub: str
    text: str


class SubsectionCreate(SubsectionBase):
    """Class that passes public instance attributes"""

    pass


class Subsection(SubsectionBase):
    """Class that defines public instance attributes"""

    id: int
    country: Country
    chapter: Chapter
    article: Article
    section: Section

    class Config:
        """Class that configures ORM mode"""

        orm_mode = True
