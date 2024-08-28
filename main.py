from fastapi import FastAPI
from routes import category_movie, tv , movie
from config.db import Base, engine, Session

from models.tv.tv_model import TvModel
from models.tv.category_tv import CategoryTv

from models.movie.movie_category import movie_category, MovieModel, CategoryModel


##### INSTANCE MY APP #####
app =  FastAPI()
app.title = 'MovieApi'

app.version = '0.0.1'


##### ROUTERS #####
app.include_router(tv.router)
app.include_router(movie.router)
app.include_router(category_movie.router)

### Motor ###
Base.metadata.create_all(bind= engine)

