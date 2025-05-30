# Contains SQLModel ORM classes which
# represent SQLModel tables

from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

# ------------------------------ #
#         Database Models        #
# ------------------------------ #

class UserInDB(SQLModel, table=True):
    __tablename__ = 'users'

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    # hashed_password : str
    items: list['ItemInDB'] = Relationship(back_populates='user')


class ItemInDB(SQLModel, table=True):
    __tablename__ = 'items'

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    image: str
    user_id: int = Field(foreign_key='users.id')
    
    user: UserInDB = Relationship(back_populates='items')
    clicks: list['ClickInDB'] = Relationship(back_populates='item')


class ClickInDB(SQLModel, table=True):
    __tablename__ = 'clicks'

    id: Optional[int] = Field(default=None, primary_key=True)
    clicked_at: Optional[datetime] = Field(default_factory=datetime.now)
    item_id: int = Field(foreign_key='items.id')

    item: ItemInDB = Relationship(back_populates='clicks')