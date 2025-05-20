from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

# ------------------------------ #
# ------- Database Models ------ #
# ------------------------------ #


# class Click(SQLModel):
#     """Represents 1 click of an item and when it occurred"""
#     id: int
#     clicked_at: datetime
#     item: Item

class UserInDB(SQLModel, table=True):
    __tablename__ = 'users'

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    # TODO what does this do?
    # chats: list["ChatInDB"] = Relationship(
    #     back_populates="users",
    #     link_model=UserChatLinkInDB,
    # )
    # hashed_password : str


class ItemInDB(SQLModel, table=True):
    __tablename__ = 'items'

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    image: str
    user: int = Field(foreign_key='users.id')


class ClickInDB(SQLModel, table=True):
    __tablename__ = 'clicks'

    id: Optional[int] = Field(default=None, primary_key=True)
    clicked_at: Optional[datetime] = Field(default_factory=datetime.now)
    item: int = Field(foreign_key='items.id')