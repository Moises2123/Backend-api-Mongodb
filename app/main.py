from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import products, carts

app = FastAPI(title="Shopping Cart API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/api/v1")
app.include_router(carts.router,    prefix="/api/v1")
