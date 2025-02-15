from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import StatusCartData
from crud import StatusCartCrud
from connections import DatabaseConnection

router = APIRouter()
crud = StatusCartCrud()
conn = DatabaseConnection()

@router.post("/status_cart/create", response_model=int)
def create(data: StatusCartData):
    """This service creates a new status cart in the database."""
    print("Creating status cart", data)
    return crud.create(data)

@router.put("/status_cart/update/{id_}", response_model=bool)
def update(id_: int, data: StatusCartData):
    """This service updates the status cart data in the database based on its id."""
    try:
        crud.update(data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.delete("/status_cart/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a status cart from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/status_cart/get_by_id/{id_}", response_model=Optional[StatusCartData])
def get_by_id(id_: int):
    """This service gets a status cart from the database based on its id."""
    return crud.get_by_id(id_)

@router.get("/status_cart/get_all", response_model=List[StatusCartData])
def get_all():
    """This service gets all the status carts from the database."""
    return crud.get_all()