from pydantic import BaseModel
from typing import Optional

class FlashcardBase(BaseModel):
    word: str
    description: Optional[str] = None
    example: Optional[str] = None
    personal_note: Optional[str] = None
    deck_id: str

class FlashcardCreate(FlashcardBase):
    pass

class FlashcardResponse(FlashcardBase):
    id: str
    user_id: str