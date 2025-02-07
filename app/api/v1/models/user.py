from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: Optional[str] = None
    email: EmailStr
    username: str
    hashed_password: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
