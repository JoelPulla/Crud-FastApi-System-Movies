from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import func
from config.db import Session


from models.movie.movie_category_model import CategoryModel,  MovieModel
from schema.movie.category import CategoryCreate, Movie

router = APIRouter()

@router.get('/movie/category', tags=['movie/category'], )
def get_all_category():
    db =  Session()
    reslts = db.query(CategoryModel).filter(CategoryModel.is_active == True).all()
    if not reslts:
        return []
    
    return reslts

@router.post('/movie/category/create', tags=['movie/category'], response_model=dict)
def create_category(category: CategoryCreate)-> dict:
    db = Session()
    filt = db.query(CategoryModel).filter(func.lower(CategoryModel.name )==  func.lower(category.name)).first()
    if filt:
        return JSONResponse({"message": "Error ya existe una categoria con ese nombre"})
    new_cat = CategoryModel(**category.model_dump())
    db.add(new_cat)
    db.commit()

    return JSONResponse(status_code=200, content= {"message":"success"})

@router.delete('/movie/category/delete/{id}', tags=['movie/category'])
def delete_category(id:int):
    
    db = Session()
    result = db.query(CategoryModel).filter(CategoryModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "no encontrado"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=202, content={"message": "eliminado con exito"})

@router.get('/movie/category/{id}/movies', tags=['movie/category'], response_model=list[Movie])
def movies_by_category(id:int):
    db = Session()
    page = 0
    
    movies = db.query(MovieModel).join(MovieModel.categories).filter(CategoryModel.id == id).all()
    
   
    # Retornar las películas de la categoría
    return movies