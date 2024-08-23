from fastapi import FastAPI
from routes import tv , movie, cat_movie
from config.db import Base, engine, Session
from models.tv.tv_model import TvModel
from schema.tv.tv_schema import Tv
from models.tv.category_tv import CategoryTv
from models.movie.movie_model import MovieModel
from models.movie.category_model import CategoryModel
from schema.movie.movie_schema import Movie
from schema.movie.category import Category

##### INSTANCE MY APP #####
app =  FastAPI()
app.title = 'MovieApi'

app.version = '0.0.1'


##### ROUTERS #####
app.include_router(tv.router)
app.include_router(movie.router)
app.include_router(cat_movie.router)

### Motor ###
Base.metadata.create_all(bind= engine)

