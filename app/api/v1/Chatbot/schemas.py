from pydantic import BaseModel
from typing import Optional

class ChatbotBase(BaseModel):
    question: str
    answer: str
    user_id: str

class ChatbotCreate(ChatbotBase):  
    pass

class ChatbotResponse(ChatbotBase):
    id: str