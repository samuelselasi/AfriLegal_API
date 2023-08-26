#!/usr/bin/python3
"""Module that defines endpoints for articles"""

import io
from typing import List
from fastapi import Depends, HTTPException, APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...),
                     db: Session = Depends(get_db)):
    """Function that defines endpoint to upload a pdf"""

    pdf_content = file.file.read()
    pdf_data = schemas.PDFCreate(title=file.filename, content=pdf_content)
    db_pdf = crud.create_pdf(db, pdf_data)
    return {"message": "PDF uploaded successfully", "pdf_id": db_pdf.id}


@router.get("/pdf/{pdf_id}/")
async def get_pdf(pdf_id: int, db: Session = Depends(get_db)):
    """Function that defines endpoint to download pdf based on id"""

    pdf = crud.get_pdf(db, pdf_id)
    if pdf:
        return StreamingResponse(io.BytesIO(pdf.content),
                                 media_type="application/pdf")
    return {"message": "PDF not found"}
