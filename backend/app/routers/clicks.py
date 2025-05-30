from fastapi import APIRouter, Depends
from sqlmodel import Session
import app.database as db
from app.entities import *

clicks_router = APIRouter(prefix='/clicks', tags=['Clicks'])


@clicks_router.get("/{click_id}", response_model=ClickResponse)
def get_click_by_id(click_id: int, session: Session = Depends(db.get_session)):
    click = db.get_click(session, click_id=click_id)
    return ClickResponse(click=click)


@clicks_router.post("/{item_id}", response_model=ClickResponse)
def create_click(item_id: int, session: Session = Depends(db.get_session)):
    click = db.create_click(session, item_id)
    return ClickResponse(click)


@clicks_router.delete("/{click_id}")
def delete_click(click_id: int, session: Session = Depends(db.get_session)):
    db.delete_click(session, click_id)


@clicks_router.get("/user/{user_id}", response_model=ClickCollection)
def get_click_by_user(
    user_id: int,
    session: Session = Depends(db.get_session)):
    clicks = db.get_clicks_by_user_id(session, user_id)
    return ClickCollection(clicks=clicks, user_id=user_id)


@clicks_router.get("/user/{user_id}/{timestamp}", response_model=ClickCollection)
def get_click_by_time(
    user_id: int,
    timestamp: datetime,
    session: Session = Depends(db.get_session)):
    db.get_clicks_by_time(session, user_id, timestamp)
