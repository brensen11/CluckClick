from pydantic import BaseModel
from typing import Optional
from sqlmodel import SQLModel, Field
from fastapi import Query
from datetime import datetime

# ----------------------------------- #
#             Data Models             #
# ----------------------------------- #
#
# Models which are used in requests or responses.
# Inherit from SQLModel for ease of casting from SQLModels
# As many of them are slimmer versions of SQLModels
#

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


class Click(SQLModel):
    """Represents 1 click of an item and when it occurred"""
    id: int
    clicked_at: datetime
    item: Item


# ----------------------------------- #
#            Request Models           #
# ----------------------------------- #
# 
# Models for Requests, meant to be used in routers
# 


class UserCreate(BaseModel):
    username: str
    email: str


class UserUpdate(BaseModel):
    username: Optional[str] = Query(None)
    email: Optional[str] = Query(None)


class ItemCreate(BaseModel):
    name: str
    image: str # TODO correct? image/file upload ... ?
    user_id: int


class ItemUpdate(BaseModel):
    name: Optional[str]
    image: Optional[str]


# ----------------------------------- #
#           Response Models           #
# ----------------------------------- #
# 
# Models for Responses, meant to be used in routers
# 

class ItemResponse(BaseModel):
    item: Item


class UserResponse(BaseModel):
    user: User


class ClickResponse(BaseModel):
    click: Click


class ItemCollection(BaseModel):
    """Represents all Items associated with a user"""
    items: list[Item]


class ClickCollection(BaseModel):
    clicks: list[Click]
