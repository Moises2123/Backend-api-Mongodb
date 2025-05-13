from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

class Product(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    price: float
    stock: int = 0

    class Config:
        populate_by_name = True
        json_encoders = {
            ObjectId: str
        }
        