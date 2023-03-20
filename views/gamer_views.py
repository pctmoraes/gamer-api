from fastapi import APIRouter, HTTPException
from services import GamerService
from schemas import *
from typing import List

gamer = APIRouter(prefix='/gamer')

@gamer.post('/post')
async def post(gamer: Gamer):
    try:
        await GamerService.post(nickname = gamer.nickname, first_name = gamer.first_name, last_name = gamer.last_name)
        return {"message":"OK"}
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@gamer.get('/all', response_model=List[GamerList])
async def get_all():
    try:
        return await GamerService.get_all()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@gamer.get('/{nickname}', response_model=GamerList)
async def get_by_id(nickname: str):
    try:
        result = await GamerService.get_by_id(nickname)
        return result
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@gamer.delete('/delete/{nickname}')
async def delete(nickname: str):
    try:
        await GamerService.delete(nickname = nickname)
        return {"message":"OK"}
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@gamer.put('/put/{nickname}')
async def put(gamer: Gamer):
    try:
        result = await GamerService.put(nickname = gamer.nickname, first_name = gamer.first_name, last_name = gamer.last_name)
        if result:
            return {"message":result}
        else:
            return {"message":result}
    except Exception as error:
        raise HTTPException(400, detail=str(error))