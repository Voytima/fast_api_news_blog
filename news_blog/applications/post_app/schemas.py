from typing import Optional
from pydantic import BaseModel
import datetime
from news_blog.applications.auth_app.schemas import User


class PostBase(BaseModel):
    title: str
    body: str


class PostList(PostBase):
    created_date: Optional[datetime.datetime]
    owner_id: int
    owner: User

    class Config:
        orm_mode = True
