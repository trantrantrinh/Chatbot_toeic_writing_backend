from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorDatabase
class ChatbotService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.collection =db["chatbot"]
    async def create_chatbot(self, chatbot_data: dict, user_id: str):
        now = datetime.utcnow()
        chatbot = {
            "question": chatbot_data["question"],
            "answer": chatbot_data.get("answer"),
            "user_id": user_id,
            "created_at": now,
            "updated_at": now
        }
        result = await self.collection.insert_one(chatbot)
        chatbot["id"] = str(result.inserted_id)
        return chatbot