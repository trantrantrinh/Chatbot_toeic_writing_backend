from fastapi import APIRouter, Depends
from .services import FlashcardService
from .schemas import FlashcardCreate, FlashcardResponse
from app.database.mongodb import get_db

router = APIRouter()

@router.post("/", response_model=FlashcardResponse)
async def create_flashcard(
    flashcard: FlashcardCreate,
    db = Depends(get_db)
):
    user_id = "test_user_id"
    flashcard_service = FlashcardService(db)
    return await flashcard_service.create_flashcard(flashcard.dict(), user_id)