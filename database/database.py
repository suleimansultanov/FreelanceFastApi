# database.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ⛔ Было так (асинхронно, но ты хочешь синхронно):
# DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/freelanceDb"

# ✅ Сделай так:
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/freelanceDb")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 