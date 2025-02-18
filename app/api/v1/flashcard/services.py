from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorDatabase

class FlashcardService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.collection = db["flashcards"]

    async def create_flashcard(self, flashcard_data: dict, user_id: str):
        now = datetime.utcnow()
        flashcard = {
            "word": flashcard_data["word"],
            "description": flashcard_data.get("description"),
            "example": flashcard_data.get("example"),
            "personal_note": flashcard_data.get("personal_note"),
            "deck_id": flashcard_data["deck_id"],
            "user_id": user_id,
            "created_at": now,
            "updated_at": now
        }
        
        result = await self.collection.insert_one(flashcard)
        flashcard["id"] = str(result.inserted_id)
        return flashcard