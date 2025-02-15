from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import TypeUserData
from crud import TypeUserCRUD
from connections import DatabaseConnection


router = APIRouter()
crud = TypeUserCRUD()
conn = DatabaseConnection()

@router.post("/type_user/create", response_model=int)
def create(data: TypeUserData):
    """This service creates a new type user in the database.
    Remember that the type user data must have the specified struture."""
    print("Creating type user", data)
    return crud.create(data)

@router.put("/type_user/update/{id_}", response_model=bool)
def update(id_: int, data: TypeUserData):
    """This service updates the type user data in the database based on its id."""
    try:
        crud.update(id_, data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    

@router.delete("/type_user/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a type user from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    
    
@router.get("/type_user/get_by_id/{id_}", response_model=Optional[TypeUserData])
def get_by_id(id_: int):
    """This service gets a type user from the database based on its id."""
    return crud.get_by_id(id_)


@router.get("/type_user/get_all", response_model=List[TypeUserData])
def get_all():
    """This service gets all the type users from the database."""
    return crud.get_all()
