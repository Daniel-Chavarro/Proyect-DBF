from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import CartItemData
from crud import CartItemCRUD
from connections import DatabaseConnection

router = APIRouter()
crud = CartItemCRUD()
conn = DatabaseConnection()

@router.post("/cart/create", response_model=int)
def create(data: CartItemData):
    """This service creates a new cart in the database."""
    print("Creating cart", data)
    return crud.create(data)

@router.put("/cart/update/{id_}", response_model=bool)
def update(data: CartItemData):
    """This service updates the cart data in the database based on its id."""
    try:
        crud.update(data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.delete("/cart/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a cart from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/cart/get_by_id/{id_}", response_model=Optional[CartItemData])
def get_by_id(id_: int):
    """This service gets a cart from the database based on its id."""
    return crud.get_by_id(id_)

@router.get("/cart/get_all", response_model=List[CartItemData])
def get_all():
    """This service gets all the carts from the database."""
    return crud.get_all()