from fastapi import FastAPI
from .routers import users, files, comments

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(files.router)
app.include_router(comments.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}