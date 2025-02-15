from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import ProductData
from crud import ProductCrud
from connections import PostgresDatabaseConnection

router = APIRouter()
crud = ProductCrud()
conn = PostgresDatabaseConnection()

@router.post("/product/create", response_model=int)
def create(data: ProductData):
    """This service creates a new product in the database."""
    print("Creating product", data)
    return crud.create(data)

@router.put("/product/update/{id_}", response_model=bool)
def update(id_: int, data: ProductData):
    """This service updates the product data in the database based on its id."""
    try:
        crud.update(data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.delete("/product/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a product from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/product/get_by_id/{id_}", response_model=Optional[ProductData])
def get_by_id(id_: int):
    """This service gets a product from the database based on its id."""
    return crud.get_by_id(id_)

@router.get("/product/get_all", response_model=List[ProductData])
def get_all():
    """This service gets all the products from the database."""
    return crud.get_all()