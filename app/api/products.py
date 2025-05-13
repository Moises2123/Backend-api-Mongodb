from fastapi import APIRouter, HTTPException
from typing import List
from bson import ObjectId
from app.db.database import db
from app.schemas import ProductIn, ProductOut

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=List[ProductOut])
async def list_products():
    cursor = db.products.find()
    return [ProductOut(**doc) async for doc in cursor]

@router.post("/", response_model=ProductOut, status_code=201)
async def create_product(product: ProductIn):
    # Inserta el producto en Mongo
    res = await db.products.insert_one(product.model_dump())
    # Recupera el documento completo (incluye "_id")
    new = await db.products.find_one({"_id": res.inserted_id})
    # Pydantic usará el alias para exponerlo como "id"
    return ProductOut(**new)

@router.get("/{product_id}", response_model=ProductOut)
async def get_product(product_id: str):
    doc = await db.products.find_one({"_id": ObjectId(product_id)})
    if doc is None:
        raise HTTPException(404, "Producto no encontrado")
    return ProductOut(**doc)
