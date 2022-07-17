from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/posts")
def get_data():
    return {"data": "welcome to posts"}


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}
