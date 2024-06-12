from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    # Comment out any problematic relationships for now
    # files = relationship("File", back_populates="owner")
    # comments = relationship("Comment", back_populates="author")

class File(Base):
    __tablename__ = "files"
    
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    file_path = Column(String)
    # Commenting out AccessLog relationship for now
    # access_logs = relationship("AccessLog", back_populates="file")

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(Integer, ForeignKey("files.id"))
    content = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))
    # Commenting out any problematic relationships for now
    # author = relationship("User", back_populates="comments")