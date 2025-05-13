from pydantic import BaseModel, Field, field_validator
from bson import ObjectId

class ProductIn(BaseModel):
    name: str
    price: float
    stock: int

class ProductOut(BaseModel):
    id: str = Field(alias="_id")
    name: str
    price: float
    stock: int

    # Este validador convierte el ObjectId de Mongo a str antes de la validación
    @field_validator("id", mode="before")
    def cast_objectid_to_str(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v

    model_config = {
        "populate_by_name": True,    # permite rellenar 'id' desde '_id'
    }
    