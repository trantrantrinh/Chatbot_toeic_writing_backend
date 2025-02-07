from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database.mongodb import MongoDB
from app.api.v1.flashcard.router import router as flashcard_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await MongoDB.connect()
    yield
    # Shutdown
    await MongoDB.close()

app = FastAPI(lifespan=lifespan)
app.include_router(flashcard_router, prefix="/api/v1/flashcard", tags=["flashcard"])