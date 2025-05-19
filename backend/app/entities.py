from pydantic import BaseModel
from typing import Optional
from sqlmodel import SQLModel
from fastapi import Query

# ----------------------------------- #
#            Request Models           #
# ----------------------------------- #


# ----------------------------------- #
#             Data Models             #
# ----------------------------------- #

class Item(SQLModel):
    id: int
    name: str
    image: str


# ----------------------------------- #
#           Response Models           #
# ----------------------------------- #