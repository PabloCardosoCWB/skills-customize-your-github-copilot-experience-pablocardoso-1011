from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Inventory API")

# In-memory data store
items = [
    {"id": 1, "name": "Laptop", "description": "Gaming laptop", "price": 1299.99, "available": True},
    {"id": 2, "name": "Mouse", "description": "Wireless mouse", "price": 49.99, "available": True},
    {"id": 3, "name": "Keyboard", "description": "Mechanical keyboard", "price": 89.99, "available": False},
]


class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    available: bool = True


# TODO: Create a GET /items endpoint that returns the list of items
# TODO: Create a GET /items/{item_id} endpoint that returns one item by ID
# TODO: Create a POST /items endpoint that adds a new item to the list
# TODO: Validate required fields and raise HTTPException when item_id is not found


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", reload=True)
