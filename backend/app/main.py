#!/usr/bin/python3
"""Module to initialize routers and endpoints"""

from fastapi import FastAPI
from app.routers.users import main as users
from app.routers.items import main as items
from app.routers.regions import main as regions
from app.routers.countries import main as countries
from app.routers.preambles import main as preambles
from app.routers.chapters import main as chapters
from app.routers.articles import main as articles
from app.routers.sections import main as sections
from app.routers.subsections import main as subsections
from app.routers.search import main as search
from app.routers.pdfs import main as pdfs

app = FastAPI()


app.include_router(regions.router, tags=["Regions"])
app.include_router(countries.router, tags=["Countries"])
app.include_router(preambles.router, tags=["Preambles"])
app.include_router(chapters.router, tags=["Chapters"])
app.include_router(articles.router, tags=["Articles"])
app.include_router(sections.router, tags=["Sections"])
app.include_router(subsections.router, tags=["Subsections"])
app.include_router(search.router, tags=["Search"])
app.include_router(pdfs.router, tags=["PDFs"])
app.include_router(users.router, tags=["Users"])
app.include_router(items.router, tags=["Items"])


@app.get("/")
async def root():
    """Function that returns a default message when the root url is hit"""
    return {"message": "Welcome to AfriLegal API"}
