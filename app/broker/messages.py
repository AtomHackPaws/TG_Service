from typing import List
from pydantic import BaseModel


class PhotoTopic(BaseModel):
    photo: List[str]
    user: str


class Data(BaseModel):
    photo: PhotoTopic
