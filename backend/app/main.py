from fastapi import FastAPI
from contextlib import asynccontextmanager

# from backend.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # create_db_and_tables()
    yield

app = FastAPI(
    title="Cluck Click API",
    description="API for tracking clicks and stuff.",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(auth_router)
