from uuid import UUID
from typing import List
from pydantic import BaseModel


class PhotoTopic(BaseModel):
    id: UUID
    photo: List[str]
    user: int


class Data(BaseModel):
    photo: PhotoTopic


class Inference(BaseModel):
    user: int
    src: List[str]
    src_marked: List[str]
