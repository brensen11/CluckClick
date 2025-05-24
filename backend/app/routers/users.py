from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.entities import *
from app.database import *
users_router = APIRouter(prefix="/users", tags=["Users"])

# ----- asdf -----


@users_router.get("/me", response_model=UserResponse)
def get_self(user: UserInDB = Depends(get_current_user)):
    return UserResponse(user=user)


@users_router.put("/me", response_model=UserResponse)
def update_self(
    update_user: UserUpdate, 
    user: UserInDB = Depends(get_current_user),
    session: Session = Depends(db.get_session)
):
    return UserResponse(user = db.update_user(session, update_user, user))


# GET /users/{user_id}
@users_router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(
    user_id: int,
    session: Session = Depends(db.get_session)
):
    """Get a User given an id"""
    return UserResponse(user=db.get_user(session, user_id))


# GET /users/{user_id}/chats
@users_router.get("/{user_id}/chats", response_model=ChatCollection)
def get_user_chats(
    user_id: int,
    session: Session = Depends(db.get_session)
):
    """Get a Collection of Chats associated with a given User id"""
    chats = db.get_chats(session, user_id)
    chats = sorted(chats, key=lambda chat: chat.name)
    return ChatCollection(meta={"count": len(chats)},
                          chats=chats)
    
    