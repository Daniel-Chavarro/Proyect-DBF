from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import AddressData
from crud import AddressCrud
from connections import PostgresDatabaseConnection

router = APIRouter()
crud = AddressCrud()
conn = PostgresDatabaseConnection()

@router.post("/address/create", response_model=int)
def create(data: AddressData):
    """This service creates a new address in the database."""
    print("Creating address", data)
    return crud.create(data)

@router.put("/address/update/{id_}", response_model=bool)
def update(id_: int, data: AddressData):
    """This service updates the address data in the database based on its id."""
    try:
        crud.update(data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.delete("/address/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes an address from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/address/get_by_id/{id_}", response_model=Optional[AddressData])
def get_by_id(id_: int):
    """This service gets an address from the database based on its id."""
    return crud.get_by_id(id_)

@router.get("/address/get_all", response_model=List[AddressData])
def get_all():
    """This service gets all the addresses from the database."""
    return crud.get_all()