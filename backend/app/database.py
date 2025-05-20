from datetime import datetime
from sqlmodel import Session, SQLModel, create_engine, select, join
import os

from app.entities import (
    UserCreate,
    UserUpdate,
    ItemCreate,
    ItemUpdate,
    ItemRemove,
    ClickCreate, 
    ClickRemove
)

from app.schema import (
    UserInDB,
    ItemInDB,
    ClickInDB
)

# if os.environ.get("DB_LOCATION") == "RDS":

db_url = "sqlite:///backend/pony_express.db"
echo = True
connect_args = {"check_same_thread": False}

engine = create_engine(
    db_url,
    echo=echo,
    connect_args=connect_args
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

# define exceptions ...
# go here ...

# ---------- users ---------- #

def create_user(session: Session, user_create: UserCreate) -> UserInDB:
    user = UserInDB(**user_create.model_dump(), created_at=datetime.now())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def update_user(session: Session, update_user: UserUpdate, user: UserInDB) -> UserInDB:
    if update_user.username:
        user.username = update_user.username
    if update_user.email:
        user.email = update_user.email
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_items(session: Session, user_id: int) -> list[ItemInDB]:
    query = select(ItemInDB).where(ItemInDB.user_id == user_id)
    return session.exec(query).all()

# ---------- items ---------- #

def get_item(session: Session, item_id: int) -> ItemInDB:
    item = session.get(ItemInDB, item_id)
    if not item:
        raise Exception("Add Exception Stuff")
    return item
def create_item(session: Session, item_create: ItemCreate):
    item = UserInDB(**item_create.model_dump(), created_at=datetime.now())
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

def update_item(session: Session, item_update: ItemUpdate, item: ItemInDB) -> ItemInDB:
    if item_update.name:
        item.name = item_update.name
    if item_update.image:
        item.image = item_update.image
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

def remove_item(session: Session, item_id: int):
    item = get_item(session, item_id)
    session.delete(item)
    session.commit()

# ----- clicks ----- #

def get_click(session: Session, click_id) -> ItemInDB:
    click = session.get(ItemInDB, click_id)
    if not click:
        raise Exception("Add Exception Stuff")
    return click

def create_click(session: Session, item_id: int) -> ClickInDB:
    click = ClickInDB(item_id=item_id)
    session.add(click)
    session.commit()
    session.refresh(click)
    return click

def remove_click(session: Session, click_id: int):
    click = get_click(session, click_id)
    session.delete(click)
    session.commit()