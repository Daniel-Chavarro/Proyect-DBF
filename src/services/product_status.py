from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import ProductStatusData
from crud import ProductStatusCrud
from connections import DatabaseConnection


router = APIRouter()
crud = ProductStatusCrud()
conn = DatabaseConnection()

@router.post("/product_status/create", response_model=int)
def create(data: ProductStatusData):
    """This service creates a new product status in the database.
    Remember that the product status data must have the specified structure."""
    print("Creating product status", data)
    return crud.create(data)

@router.put("/product_status/update/{id_}", response_model=bool)
def update(id_: int, data: ProductStatusData):
    """This service updates the product status data in the database based on its id."""
    try:
        crud.update(id_, data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    

@router.delete("/product_status/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a product status from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    
    
@router.get("/product_status/get_by_id/{id_}", response_model=Optional[ProductStatusData])
def get_by_id(id_: int):
    """This service gets a product status from the database based on its id."""
    return crud.get_by_id(id_)


@router.get("/product_status/get_all", response_model=List[ProductStatusData])
def get_all():
    """This service gets all the product statuses from the database."""
    return crud.get_all()

@router.get("/product_status/get_by_name/{name}", response_model=Optional[ProductStatusData])
def get_by_name(name: str):
    """This service gets a product status from the database based on its name."""
    return crud.get_by_name(name)