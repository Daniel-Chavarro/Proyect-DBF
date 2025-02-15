from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import FavoriteListUserStoreData
from crud import FavoriteListUserStoreCRUD
from connections import DatabaseConnection

router = APIRouter()
crud = FavoriteListUserStoreCRUD()
conn = DatabaseConnection()

@router.post("/favorite_list_user_store/create", response_model=int)
def create(data: FavoriteListUserStoreData):
    """This service creates a new favorite list user store in the database."""
    print("Creating favorite list user store", data)
    return crud.create(data)

@router.put("/favorite_list_user_store/update/{id_}", response_model=bool)
def update(id_: int, data: FavoriteListUserStoreData):
    """This service updates the favorite list user store data in the database based on its id."""
    try:
        crud.update(data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.delete("/favorite_list_user_store/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a favorite list user store from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/favorite_list_user_store/get_by_id/{id_}", response_model=Optional[FavoriteListUserStoreData])
def get_by_id(id_: int):
    """This service gets a favorite list user store from the database based on its id."""
    return crud.get_by_id(id_)

@router.get("/favorite_list_user_store/get_all", response_model=List[FavoriteListUserStoreData])
def get_all():
    """This service gets all the favorite list user stores from the database."""
    return crud.get_all()