from fastapi import APIRouter, HTTPException
from services import CharacterService
from schemas import *
from typing import List

character = APIRouter(prefix='/character')

@character.post('/post')
async def character_post(character: Character):
    try:
        await CharacterService.create(name=character.name, gamer_nickname=character.gamer_nickname)
        return {"message":"OK"}
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@character.get('/all', response_model=List[Character])
async def get_all():
    try:
        return await CharacterService.get_all()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@character.get('/{name}', response_model=Character)
async def get_by_id(name: str):
    try:
        result = await CharacterService.get_by_id(name)
        return result
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@character.delete('/delete/{name}')
async def delete(name: str):
    try:
        await CharacterService.delete(name = name)
        return {"message":"OK"}
    except Exception as error:
        raise HTTPException(400, detail=str(error))
