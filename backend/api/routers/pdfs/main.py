#!/usr/bin/python3
"""Module that defines endpoints to download pdfs"""

import io
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.responses import StreamingResponse
from fastapi import Depends, APIRouter, File, UploadFile

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/download_pdf/{pdf_id}/")
async def get_pdf_by_id(pdf_id: int, db: Session = Depends(get_db)):
    """Endpoint to download a constitution pdf based on its id"""

    pdf = crud.get_pdf_id(db, pdf_id)
    if pdf:
        return StreamingResponse(io.BytesIO(pdf.content),
                                 media_type="application/pdf")
    return {"message": "PDF not found"}


@router.get("/download_pdf/pdf_title")
async def get_pdf_by_title(pdf_title: str, db: Session = Depends(get_db)):
    """Endpoint to download a constitution pdf based on its title"""

    pdf = crud.get_pdf_title(db, pdf_title)
    if pdf:
        return StreamingResponse(io.BytesIO(pdf.content),
                                 media_type="application/pdf")
    return {"message": "PDF not found"}


@router.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...),
                     db: Session = Depends(get_db)):
    """Endpoint to upload a constitution pdf"""

    pdf_content = file.file.read()
    pdf_data = schemas.PDFCreate(title=file.filename, content=pdf_content)
    db_pdf = crud.create_pdf(db, pdf_data)
    return {"message": "PDF uploaded successfully", "pdf_id": db_pdf.id}
