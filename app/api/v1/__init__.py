from fastapi import APIRouter
from .Chatbot.router import router as chatbot_router

router = APIRouter()
router.include_router(chatbot_router, prefix="/chatbot", tags=["chatbot"])
