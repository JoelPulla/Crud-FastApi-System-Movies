from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.db import Session
from models.movie.category_model import CategoryModel
from schema.movie.category import Category


router = APIRouter()


@router.get('/movie/category', tags=['movie/category'], )
def get_all_category():
    db =  Session()
    reslts = db.query(CategoryModel).all()
    
    return reslts

@router.post('/movie/category/create', tags=['movie/category'], response_model=dict)
def create_category(category: Category)-> dict:
    
    db = Session()
    filt = db.query(CategoryModel).filter(CategoryModel.name == category.name).first()
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