from asyncio import run
from connection import engine
import models

async def create_database():
    async with engine.begin() as connection:
        await connection.run_sync(models.Base.metadata.drop_all)
        await connection.run_sync(models.Base.metadata.create_all)

if __name__ == '__main__':
    run(create_database())