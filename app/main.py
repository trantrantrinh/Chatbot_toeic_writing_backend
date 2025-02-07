from fastapi import FastAPI, Depends, HTTPException
from app.database.mongodb import get_db
from app.api.v1.auth.login.router import router as login_router
from app.api.v1.auth.register.router import router as register_router
from app.api.v1.flashcard.router import router as flashcard_router

app = FastAPI()

#test the connection to the database
@app.get("/test-db")
async def test_db_connection(db=Depends(get_db)):
    try:
        # Thực hiện một truy vấn đơn giản để kiểm tra kết nối
        result = await db.command("ping")
        return {"status": "success", "message": "Connected to MongoDB", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to MongoDB: {e}")

# Include routers
app.include_router(login_router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(register_router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(flashcard_router, prefix="/api/v1/flashcard", tags=["flashcard"])