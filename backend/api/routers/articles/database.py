#!/usr/bin/python3
"""Module that defines PostgreSQL database URL"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:sel@localhost/test"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:afrilegalpwd@100.26.231.45/test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
