from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import DeliveryStatusData
from crud import DeliveryStatusCRUD
from connections import PostgresDatabaseConnection


router = APIRouter()
crud = DeliveryStatusCRUD()
conn = PostgresDatabaseConnection()

@router.post("/delivery_status/create", response_model=int)
def create(data: DeliveryStatusData):
    """This service creates a new delivery status in the database.
    Remember that the delivery status data must have the specified structure."""
    print("Creating delivery status", data)
    return crud.create(data)

@router.put("/delivery_status/update/{id_}", response_model=bool)
def update(id_: int, data: DeliveryStatusData):
    """This service updates the delivery status data in the database based on its id."""
    try:
        crud.update(id_, data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    

@router.delete("/delivery_status/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a delivery status from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    
    
@router.get("/delivery_status/get_by_id/{id_}", response_model=Optional[DeliveryStatusData])
def get_by_id(id_: int):
    """This service gets a delivery status from the database based on its id."""
    return crud.get_by_id(id_)


@router.get("/delivery_status/get_all", response_model=List[DeliveryStatusData])
def get_all():
    """This service gets all the delivery statuses from the database."""
    return crud.get_all()

@router.get("/delivery_status/get_by_name/{name}", response_model=Optional[DeliveryStatusData])
def get_by_name(name: str):
    """This service gets a delivery status from the database based on its name."""
    return crud.get_by_name(name)