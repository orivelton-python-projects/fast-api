from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
  title: str
  content: str
  published: bool = True
  rating: Optional[int] = None
  
my_post = [{
  "id": 1,
  "title": "title",
  "content": "content"
}]

@app.get("/")
def root():
  return { "message": "Hello World" }

@app.get("/posts")
def get_posts():
  return { "data": "This is a post"}

@app.post("/createposts")
def create_posts(new_post: Post):
  print(new_post)
  return { "data": "new post"}
