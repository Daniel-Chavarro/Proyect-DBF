from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import StoreData
from crud import StoreCrud
from connections import PostgresDatabaseConnection

router = APIRouter()
crud = StoreCrud()
conn = PostgresDatabaseConnection()

@router.post("/store/create", response_model=int)
def create(data: StoreData):
    """This service creates a new store in the database."""
    print("Creating store", data)
    return crud.create(data)

@router.put("/store/update/{id_}", response_model=bool)
def update(id_: int, data: StoreData):
    """This service updates the store data in the database based on its id."""
    try:
        crud.update(data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.delete("/store/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a store from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/store/get_by_id/{id_}", response_model=Optional[StoreData])
def get_by_id(id_: int):
    """This service gets a store from the database based on its id."""
    return crud.get_by_id(id_)

@router.get("/store/get_all", response_model=List[StoreData])
def get_all():
    """This service gets all the stores from the database."""
    return crud.get_all()