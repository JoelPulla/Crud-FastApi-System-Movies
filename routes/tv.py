from fastapi import APIRouter 
from fastapi.responses import JSONResponse
from config.db import Session
from schema.tv.tv_schema import Tv
from models.tv.tv_model import TvModel

router = APIRouter()

@router.post('/tv', tags=['tv'], response_model=dict, status_code=200)
def createTv(tv: Tv) -> dict:
    db = Session()
    new_tv = TvModel(**tv.model_dump())
    db.add(new_tv)
    db.commit() 
    return JSONResponse( status_code= 201, content={"message": "succes"})

@router.get('/tv', tags=['tv'], response_model=list[Tv])
def getAllTv()-> list[Tv]:
    db = Session()
    resul =  db.query(TvModel).all()
    return resul
     
@router.delete('/tv/{id}', tags=['tv'], )
def deleteTv(id: int):
    db = Session()
    tv = db.query(TvModel).filter(TvModel.id == id).first()
    if not tv:
        return JSONResponse(status_code=404, content={"message": "Tv no encontrada"})
    db.delete(tv)
    db.commit()
    return JSONResponse(status_code=200, content= {"message":"succes"})

@router.put('/tv/{id}', tags=['tv'], response_model=dict, status_code=200)
def editTv(id:int, tv: Tv)-> dict:
    db = Session()
    result = db.query(TvModel).filter(TvModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404,content= {"message":"tv no econtrada"})
    
    result.name = tv.name
    result.info = tv.info
    result.url_stream = tv.url_stream
    result.is_active = tv.is_active
    db.commit()
    
    return  JSONResponse(status_code= 200, content={"message":"success"})