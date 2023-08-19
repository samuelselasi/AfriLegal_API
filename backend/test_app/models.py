"""Module that defines tables"""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    """Class that defines users attributes"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    """Class that defines items attributes"""

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Region(Base):
    """Class that defines regions attributes"""

    __tablename__ = "regions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    countries = relationship("Country", back_populates="region")


class Country(Base):
    """Class that defines countries attributes"""

    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    region_id = Column(Integer, ForeignKey("regions.id"))

    region = relationship("Region", back_populates="countries")
    preambles = relationship("Preamble", back_populates="country")
    chapter = relationship("Chapter", back_populates="country")
    articles = relationship("Article", back_populates="country")
    sections = relationship("Section", back_populates="country")
    subsections = relationship("Subsection", back_populates="country")


class Preamble(Base):
    """Class that defines preambles attributes"""

    __tablename__ = "preamble"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    country_id = Column(Integer, ForeignKey("countries.id"))

    country = relationship("Country", back_populates="preambles")


class Chapter(Base):
    """Class that defines chapters attributes"""

    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    text = Column(String)
    country_id = Column(Integer, ForeignKey("countries.id"))

    country = relationship("Country", back_populates="chapter")
    articles = relationship("Article", back_populates="chapter")
    sections = relationship("Section", back_populates="chapter")
    subsections = relationship("Subsection", back_populates="chapter")


class Article(Base):
    """Class that defines articles attributes"""

    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    country_id = Column(Integer, ForeignKey("countries.id"))
    chapter_id = Column(Integer, ForeignKey("chapters.id"))
    number = Column(Integer)
    title = Column(String, index=True)
    text = Column(String)

    country = relationship("Country", back_populates="articles")
    chapter = relationship("Chapter", back_populates="articles")
    sections = relationship("Section", back_populates="article")
    subsections = relationship("Subsection", back_populates="article")


class Section(Base):
    """Class that defines sections attributes"""

    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)
    country_id = Column(Integer, ForeignKey("countries.id"))
    chapter_id = Column(Integer, ForeignKey("chapters.id"))
    article_id = Column(Integer, ForeignKey("articles.id"))
    number = Column(Integer)
    text = Column(String)

    country = relationship("Country", back_populates="sections")
    chapter = relationship("Chapter", back_populates="sections")
    article = relationship("Article", back_populates="sections")
    subsections = relationship("Subsection", back_populates="section")


class Subsection(Base):
    """Class that defines subsections attributes"""

    __tablename__ = "subsections"

    id = Column(Integer, primary_key=True, index=True)
    country_id = Column(Integer, ForeignKey("countries.id"))
    chapter_id = Column(Integer, ForeignKey("chapters.id"))
    article_id = Column(Integer, ForeignKey("articles.id"))
    section_id = Column(Integer, ForeignKey("sections.id"))
    sub = Column(String)
    text = Column(String)

    country = relationship("Country", back_populates="subsections")
    chapter = relationship("Chapter", back_populates="subsections")
    article = relationship("Article", back_populates="subsections")
    section = relationship("Section", back_populates="subsections")
