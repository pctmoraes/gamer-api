from fastapi import FastAPI
from views import gamer_views, character_views

app = FastAPI()

@app.get('/')
def home():
    return('hello world!')

app.include_router(gamer_views.gamer)
app.include_router(character_views.character)