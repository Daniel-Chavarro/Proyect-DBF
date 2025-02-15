from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import BrandData
from crud import BrandCRUD
from connections import PostgresDatabaseConnection


router = APIRouter()
crud = BrandCRUD()
conn = PostgresDatabaseConnection()

@router.post("/brand/create", response_model=int)
def create(data: BrandData):
    """This service creates a new brand in the database.
    Remember that the brand data must have the specified structure."""
    print("Creating brand", data)
    return crud.create(data)

@router.put("/brand/update/{id_}", response_model=bool)
def update(id_: int, data: BrandData):
    """This service updates the brand data in the database based on its id."""
    try:
        crud.update(id_, data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    

@router.delete("/brand/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a brand from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    
    
@router.get("/brand/get_by_id/{id_}", response_model=Optional[BrandData])
def get_by_id(id_: int):
    """This service gets a brand from the database based on its id."""
    return crud.get_by_id(id_)


@router.get("/brand/get_all", response_model=List[BrandData])
def get_all():
    """This service gets all the brands from the database."""
    return crud.get_all()

@router.get("/brand/get_by_name/{name}", response_model=Optional[BrandData])
def get_by_name(name: str):
    """This service gets a brand from the database based on its name."""
    return crud.get_by_name(name)