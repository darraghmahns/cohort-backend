from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.dependencies import get_db

router = APIRouter(
    prefix="/comments",
    tags=["comments"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Comment)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment)

@router.get("/{comment_id}", response_model=schemas.Comment)
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud.get_comment(db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment