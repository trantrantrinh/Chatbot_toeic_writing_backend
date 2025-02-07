import pytest
import asyncio
from typing import AsyncGenerator
from httpx import AsyncClient
from app.main import app
from app.database.mongodb import MongoDB

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
async def async_client() -> AsyncGenerator:
    """Async client for testing."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture(autouse=True)
async def setup_db():
    """Setup test database before each test."""
    # Override database name for testing
    MongoDB.DATABASE_NAME = "test_db"
    await MongoDB.connect()
    yield
    # Cleanup after test
    if MongoDB.client:
        await MongoDB.client.drop_database(MongoDB.DATABASE_NAME)
        await MongoDB.close()
