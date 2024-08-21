from fastapi import FastAPI
from routes import tv 
from config.db import Base, engine, Session
from models.tv_model import TvModel
from schema.tv_schema import Tv
from models.category_tv import CategoryTv

##### INSTANCE MY APP #####
app =  FastAPI()
app.title = 'MovieApi'

app.version = '0.0.1'

##### ROUTERS #####
app.include_router(tv.router)

### Motor ###
Base.metadata.create_all(bind= engine)

