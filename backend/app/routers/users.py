from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.entities import *
import app.database as db


users_router = APIRouter(prefix="/users", tags=["Users"])


# @users_router.get("/me", response_model=UserResponse)
# def get_self(user: UserInDB = Depends(get_current_user)):
#     return UserResponse(user=user)


# @users_router.put("/me", response_model=UserResponse)
# def update_self(
#     update_user: UserUpdate, 
#     user: UserInDB = Depends(get_current_user),
#     session: Session = Depends(db.get_session)
# ):
#     return UserResponse(user = db.update_user(session, update_user, user))


@users_router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(
    user_id: int,
    session: Session = Depends(db.get_session)
):
    """Get a User given an id"""
    return UserResponse(user=db.get_user(session, user_id))

@users_router.post("/")    
def create_user(
    user_create: UserCreate,
    session: Session = Depends(db.get_session)
):
    db.create_user(session, user_create)