#!/usr/bin/python3
"""Module that defines tables"""

from .database import Base
from sqlalchemy import LargeBinary
from sqlalchemy import Column, Integer, String


class PDFDocument(Base):
    """Class that defines pdf attributes"""
    __tablename__ = "pdf_documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(LargeBinary)
