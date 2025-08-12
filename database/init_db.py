# import asyncio
# from sqlalchemy.ext.asyncio import create_async_engine
# from database.models import Base

# DATABASE_URL = "postgresql+asyncpg://postgres:postgres@db:5432/freelanceDb"
# engine = create_async_engine(DATABASE_URL, echo=True)

# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     print("Database tables created.")

# if __name__ == "__main__":
#     asyncio.run(init_db())


# "alembic revision --autogenerate -m "'add message model'"\
# "