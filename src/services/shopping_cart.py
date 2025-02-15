from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import ShoppingCartData
from crud import ShoppingCartCrud
from connections import PostgresDatabaseConnection

router = APIRouter()
crud = ShoppingCartCrud()
conn = PostgresDatabaseConnection()

@router.post("/shopping_cart/create", response_model=int)
def create(data: ShoppingCartData):
    """This service creates a new shopping cart in the database."""
    print("Creating shopping cart", data)
    return crud.create(data)

@router.put("/shopping_cart/update/{id_}", response_model=bool)
def update(id_: int, data: ShoppingCartData):
    """This service updates the shopping cart data in the database based on its id."""
    try:
        crud.update(data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.delete("/shopping_cart/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a shopping cart from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/shopping_cart/get_by_id/{id_}", response_model=Optional[ShoppingCartData])
def get_by_id(id_: int):
    """This service gets a shopping cart from the database based on its id."""
    return crud.get_by_id(id_)

@router.get("/shopping_cart/get_all", response_model=List[ShoppingCartData])
def get_all():
    """This service gets all the shopping carts from the database."""
    return crud.get_all()