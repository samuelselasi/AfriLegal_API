#!/usr/bin/python3
"""Module to initialize routers and endpoints"""

from fastapi import FastAPI
from api.routers.auth import main as auth
from api.routers.user import main as user
from api.routers.users import main as users
from api.routers.items import main as items
from api.routers.regions import main as regions
from api.routers.countries import main as countries
from api.routers.preambles import main as preambles
from api.routers.chapters import main as chapters
from api.routers.articles import main as articles
from api.routers.sections import main as sections
from api.routers.subsections import main as subsections
from api.routers.search import main as search
from api.routers.pdfs import main as pdfs

app = FastAPI()


app.include_router(auth.router, tags=["Authentication"])
app.include_router(user.router, tags=["User"])
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
