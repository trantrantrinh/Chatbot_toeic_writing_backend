from fastapi import APIRouter, Depends, HTTPException
from .schemas import LoginRequest, LoginResponse
from app.database.mongodb import get_db

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest, db=Depends(get_db)):
    # Add login logic here
    pass
