from typing import List
from pydantic import BaseModel


class PhotoTopic(BaseModel):
    id: str
    photo: List[str]
    user: int


class Data(BaseModel):
    photo: PhotoTopic
