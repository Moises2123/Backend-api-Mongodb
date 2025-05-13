from fastapi import APIRouter
from bson import ObjectId
from app.db.database import db

router = APIRouter(prefix="/carts", tags=["Carts"])

@router.post("/{user_id}/items/{product_id}")
async def add_item(user_id: str, product_id: str, qty: int = 1):
    cart = await db.carts.find_one_and_update(
        {"user_id": user_id},
        {"$inc": {f"items.{product_id}": qty}},
        upsert=True,
        return_document=True,
    )
    return cart
