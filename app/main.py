from fastapi import FastAPI, Depends, HTTPException
from app.database.mongodb import get_db


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