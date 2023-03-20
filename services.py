from database.models import Gamer, Character
from database.connection import async_session
from sqlalchemy import delete
from sqlalchemy.future import select

class GamerService:
    async def post(nickname: str, first_name: str, last_name: str):
        async with async_session() as session:
            session.add(Gamer(nickname = nickname, first_name = first_name, last_name = last_name))
            await session.commit()

    async def get_all():
        async with async_session() as session:
            result = await session.execute(select(Gamer))
            return result.scalars().all()

    async def get_by_id(nickname: str):
        async with async_session() as session:
            result = await session.execute(select(Gamer).where(Gamer.nickname == nickname))
            return result.scalar()
    
    async def delete(nickname: str):
        async with async_session() as session:
            await session.execute(delete(Gamer).where(Gamer.nickname == nickname))
            await session.commit()
    
    async def put(nickname: str, first_name: str, last_name: str):
        async with async_session() as session:
            gamer = (await session.execute(select(Gamer).where(Gamer.nickname == nickname))).scalar()

            if gamer:
                gamer.nickname = gamer.nickname
                gamer.first_name = first_name
                gamer.last_name = last_name
                await session.commit()
                return 'Gamer updated successfuly'
            else:
                return 'Gamer not found'

# CHARACTER
class CharacterService:
    async def create(name: str, gamer_nickname: str):
        async with async_session() as session:
            session.add(Character(name=name, gamer_nickname=gamer_nickname))
            await session.commit()

    async def get_all():
        async with async_session() as session:
            result = await session.execute(select(Character))
            return result.scalars().all()

    async def get_by_id(name: str):
        async with async_session() as session:
            result = await session.execute(select(Character).where(Character.name==name))
            return result.scalar()
    
    async def delete(name: str):
        async with async_session() as session:
            await session.execute(delete(Character).where(Character.name == name))
            await session.commit()
    