from pydantic import BaseModel
from typing import Optional
from sqlmodel import SQLModel, ForeignKey
from fastapi import Query
from datetime import datetime

# ----------------------------------- #
#            Request Models           #
# ----------------------------------- #

class UserCreate(BaseModel):
    id: int

class UserUpdate(BaseModel):
    username: Optional[str] = Query(None)
    email: Optional[str] = Query(None)

class ItemAdd(BaseModel):
    name: str
    image: str # TODO correct? image/file upload ... ?

class ItemUpdate(BaseModel):
    id: int
    name: str
    image: str

class ItemRemove(BaseModel):
    id: int

class ClickAdd(BaseModel):
    item_id: int

class ClickRemove(BaseModel):
    click_id: int


# ----------------------------------- #
#             Data Models             #
# ----------------------------------- #

class User(SQLModel):
    """Represents a User in the DB and as returned by the API"""
    id: int
    username: str
    email: str
    created_at: datetime


class Item(SQLModel):
    """Represents an Item a user can track"""
    id: int
    name: str
    image: str
    user: User

class Click(SQLModel):
    """Represents 1 click of an item and when it occurred"""
    id: int
    clicked_at: datetime
    item: Item


# ----------------------------------- #
#           Response Models           #
# ----------------------------------- #

class ItemCollection(BaseModel):
    """Represents all Items associated with a user"""
    items: list[Item]
    user: ForeignKey[User]