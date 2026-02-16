from fastapi import FastAPI
from pydantic import BaseModel
import datetime

app = FastAPI(title="My Containerized API")

# In-memory storage
items = []

class Item(BaseModel):
    name: str
    description: str | None = None

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Containerized API!",
        "timestamp": datetime.datetime.now().isoformat(),
        "endpoints": {
            "GET /": "This message",
            "GET /health": "Health check",
            "GET /items": "List all items",
            "POST /items": "Create an item",
            "GET /docs": "Interactive API documentation"
        }
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.get("/items")
def list_items():
    return {"items": items, "count": len(items)}

@app.post("/items")
def create_item(item: Item):
    item_dict = item.model_dump()
    item_dict["id"] = len(items) + 1
    item_dict["created_at"] = datetime.datetime.now().isoformat()
    items.append(item_dict)
    return item_dict

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}, 404