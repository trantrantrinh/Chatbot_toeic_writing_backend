import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from app.main import app
from datetime import datetime

@pytest.mark.asyncio
async def test_create_flashcard():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Test data
        flashcard_data = {
            "word": "Hello",
            "description": "A greeting",
            "example": "Hello, how are you?",
            "personal_note": "Common greeting",
            "deck_id": "default_deck"
        }

        response = await ac.post("/api/v1/flashcard/", json=flashcard_data)
        
        # Assert response status code is 200
        assert response.status_code == 200

        # Assert response data contains expected fields
        data = response.json()
        assert data["word"] == flashcard_data["word"]
        assert data["description"] == flashcard_data["description"]
        assert data["example"] == flashcard_data["example"]
        assert data["personal_note"] == flashcard_data["personal_note"]
        assert data["deck_id"] == flashcard_data["deck_id"]
        assert "id" in data
        assert "user_id" in data
        assert data["user_id"] == "test_user_id"
        assert "created_at" in data
        assert "updated_at" in data

@pytest.mark.asyncio
async def test_create_flashcard_minimal():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Test with only required fields
        minimal_data = {
            "word": "Test",
            "deck_id": "default_deck"
        }

        response = await ac.post("/api/v1/flashcard/", json=minimal_data)
        assert response.status_code == 200
        
        data = response.json()
        assert data["word"] == minimal_data["word"]
        assert data["description"] is None
        assert data["example"] is None
        assert data["personal_note"] is None
        assert data["deck_id"] == minimal_data["deck_id"]
        assert "id" in data
        assert "user_id" in data
        assert data["user_id"] == "test_user_id"