from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import create_db_and_tables
from app.routers.items import items_router
from app.routers.users import users_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(
    title="Cluck Click API",
    description="API for tracking clicks and stuff.",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(items_router)
app.include_router(users_router)
