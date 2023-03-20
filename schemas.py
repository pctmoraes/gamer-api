from pydantic import BaseModel
from typing import List

class Gamer(BaseModel):
    nickname: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True

class Character(BaseModel):
    name: str
    gamer_nickname: str

    class Config:
        orm_mode = True

class GamerList(BaseModel):
    nickname: str
    first_name: str
    last_name: str
    characters: List[Character]

    class Config:
        orm_mode = True

    