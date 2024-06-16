from uuid import UUID
from typing import List
from pydantic import BaseModel


class PhotoTopic(BaseModel):
    id: UUID
    photo: List[str]
    user: int


class Data(BaseModel):
    photo: PhotoTopic
