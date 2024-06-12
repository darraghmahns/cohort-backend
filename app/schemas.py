from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class FileBase(BaseModel):
    file_path: str

class FileCreate(FileBase):
    pass

class File(FileBase):
    id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    file_id: int
    author_id: int

    model_config = ConfigDict(from_attributes=True)