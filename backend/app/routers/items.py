from fastapi import APIRouter, Depends
from sqlmodel import Session
import app.database as db
from app.entities import *

items_router = APIRouter(prefix='/items', tags=['Items'])


@items_router.get("/{item_id}", response_model=ItemResponse)
def get_item_by_id(item_id: int, session: Session = Depends(db.get_session)):
    item = db.get_item(session, item_id)
    return ItemResponse(item=item)


@items_router.get("/user/{user_id}", response_model=ItemCollection)
def get_items_by_user(user_id: int, session: Session = Depends(db.get_session)):
    items = db.get_items(session, user_id)
    return ItemCollection(items=items, user_id=user_id)


@items_router.post("/", response_model=ItemResponse)
def create_item(item_create: ItemCreate, session: Session = Depends(db.get_session)):
    item = db.create_item(session, item_create=item_create)
    return ItemResponse(item=item)


@items_router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item_update: ItemUpdate, session: Session = Depends(db.get_session)):
    item = db.get_item(session, item_id=item_id)
    item = db.update_item(session, item_update, item)
    return ItemResponse(item=item)


@items_router.delete("/{item_id}")
def delete_item(item_id: int, session: Session = Depends(db.get_session)):
    db.delete_item(session, item_id)

    