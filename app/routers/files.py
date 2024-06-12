from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.dependencies import get_db

router = APIRouter(
    prefix="/files",
    tags=["files"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.File)
def create_file(file: schemas.FileCreate, db: Session = Depends(get_db)):
    return crud.create_file(db=db, file=file)

@router.get("/{file_id}", response_model=schemas.File)
def read_file(file_id: int, db: Session = Depends(get_db)):
    db_file = crud.get_file(db, file_id=file_id)
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return db_file