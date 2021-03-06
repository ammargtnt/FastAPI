import uvicorn
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "hello all World"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}    
