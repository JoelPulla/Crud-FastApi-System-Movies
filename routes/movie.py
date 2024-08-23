from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.db import Session
from datetime import datetime, timedelta

from schema.movie_schema import Movie
from models.movie_model import MovieModel

router = APIRouter()
#Colsult All Movies

### Goblar var pagination ###
limit_results:int = 20


@router.get('/movie/all_movie', tags=['movie'], status_code= 200, )
def get_all_movies(page: int):
    
    db = Session()
    total_results= db.query(MovieModel).count()
    offset = (page-1)*limit_results
    total_pages = (total_results // limit_results ) +(1 if total_results % limit_results > 0 else 0)
    result = db.query(MovieModel).offset(offset).limit(limit_results).all()
    
    return {
        "page":page,
        "result": result,
        "total_page": total_pages,
        "total_results":total_results    
    }

@router.get('/search/movie', tags=['movie'])
def search_movie_name(name: str)-> list[Movie]:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.movie_title.ilike(f"%{name}%")).all()
    if not result:
        return []
    return result
   
#now Playind and pagination#   
@router.get('/movie/now_playing', tags=['movie'])  
def now_playing(page: int):
    
    db = Session()
    total_results= db.query(MovieModel).count()
    offset = (page-1)*limit_results
    total_page = (total_results // limit_results)+ (1 if total_results % limit_results > 0 else 0)
    
    now_playing = db.query(MovieModel).order_by(MovieModel.created_at.desc()).offset(offset).limit(limit_results).all()
    return {
        "page": page,
        "oofset": offset,
        "results": now_playing,
        "total items": total_results,
        "total_pages": total_page
    } 


    
#Cretae Movies
@router.post('/movie/create', tags=['movie'], status_code=200, response_model= dict)
def create_movie(movie: Movie) -> dict:
    db = Session()
    new_movie = MovieModel(**movie.model_dump())
    db.add(new_movie)
    db.commit()
    
    return JSONResponse(status_code=200, content= {"messagge": "success"})

#Delete Movies
@router.delete('/movie/delete/{id}',tags=['movie'])
def delete_movie(id:int):
    db = Session()
    
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        JSONResponse(status_code=404, content={"message": "movie no econtrada"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "delete movie"})

@router.put('/movie/update/{id}', tags=['movie'])
def update_movie(id: int, movie: Movie)-> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        JSONResponse(status_code=404, content={"message":"movie no encontrada"})
    
    result.movie_title = movie.movie_title
    result.overview = movie.overview
    result.id_tmdb = movie.id_tmdb
    result.url_video = movie.url_video
    result.is_youtube = movie.is_youtube
    result.poster_path = movie.poster_path
    result.background_path = movie.background_path
    result.voute_range = movie.voute_range
    result.popularity = movie.popularity
    result.created_at = movie.created_at
    result.release = movie.release
    
    db.commit()
    
    return JSONResponse( status_code=200, content={"message": "success"})
    
