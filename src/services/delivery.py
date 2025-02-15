from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import DeliveryData
from crud import DeliveryCRUD
from connections import DatabaseConnection

router = APIRouter()
crud = DeliveryCRUD()
conn = DatabaseConnection()

@router.post("/delivery/create", response_model=int)
def create(data: DeliveryData):
    """This service creates a new delivery in the database."""
    print("Creating delivery", data)
    return crud.create(data)

@router.put("/delivery/update/{id_}", response_model=bool)
def update(id_: int, data: DeliveryData):
    """This service updates the delivery data in the database based on its id."""
    try:
        crud.update(data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.delete("/delivery/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a delivery from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/delivery/get_by_id/{id_}", response_model=Optional[DeliveryData])
def get_by_id(id_: int):
    """This service gets a delivery from the database based on its id."""
    return crud.get_by_id(id_)

@router.get("/delivery/get_all", response_model=List[DeliveryData])
def get_all():
    """This service gets all the deliveries from the database."""
    return crud.get_all()