from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class FlashcardBase(BaseModel):
    front: str
    back: str
    deck_id: str

class FlashcardCreate(FlashcardBase):
    pass

class Flashcard(FlashcardBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime
