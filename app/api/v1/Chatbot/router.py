from fastapi import APIRouter, Depends
from .services import ChatbotService
from .schemas import ChatbotCreate, ChatbotResponse
from app.database.mongodb import get_db

router = APIRouter()

@router.post("/", response_model=ChatbotResponse)
async def create_chatbot(
    chatbot: ChatbotCreate,
    db = Depends(get_db)
):
    user_id = "test_user_id"
    chatbot_service = ChatbotService(db)
    return await chatbot_service.create_chatbot(chatbot.dict(), user_id)