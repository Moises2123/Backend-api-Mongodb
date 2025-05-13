from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import get_settings

_settings = get_settings()

client = AsyncIOMotorClient(_settings.mongodb_uri)
db = client[_settings.mongodb_db]
