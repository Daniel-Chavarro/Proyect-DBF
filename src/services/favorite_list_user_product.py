from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import FavoriteListUserProductData
from crud import FavoriteListUserProductCRUD
from connections import DatabaseConnection

router = APIRouter()
crud = FavoriteListUserProductCRUD()
conn = DatabaseConnection()

@router.post("/favorite_list_user_product/create", response_model=int)
def create(data: FavoriteListUserProductData):
    """This service creates a new favorite list user product in the database."""
    print("Creating favorite list user product", data)
    return crud.create(data)

@router.put("/favorite_list_user_product/update/{id_}", response_model=bool)
def update(id_: int, data: FavoriteListUserProductData):
    """This service updates the favorite list user product data in the database based on its id."""
    try:
        crud.update(data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.delete("/favorite_list_user_product/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a favorite list user product from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/favorite_list_user_product/get_by_id/{id_}", response_model=Optional[FavoriteListUserProductData])
def get_by_id(id_: int):
    """This service gets a favorite list user product from the database based on its id."""
    return crud.get_by_id(id_)

@router.get("/favorite_list_user_product/get_all", response_model=List[FavoriteListUserProductData])
def get_all():
    """This service gets all the favorite list user products from the database."""
    return crud.get_all()