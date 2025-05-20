from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from app.entities import *

items_router = APIRouter(prefix='/items', tags=['Items'])

# GET /items