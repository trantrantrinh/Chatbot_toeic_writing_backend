from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.mongodb import MongoDB
from app.api.v1.flashcard.router import router as flashcard_router
from .api.v1 import router as v1_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await MongoDB.connect()
    yield
    # Shutdown
    await MongoDB.close()

app = FastAPI(lifespan=lifespan)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(flashcard_router, prefix="/api/v1/flashcard", tags=["flashcard"])
app.include_router(v1_router, prefix="/api/v1")