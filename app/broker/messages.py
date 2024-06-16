from typing import List
from pydantic import BaseModel


class PhotoTopic(BaseModel):
    photo: List[str]
    user: int


class Data(BaseModel):
    id: str
    photo: PhotoTopic
