from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import DeliveryProviderData
from crud import DeliveryProviderCRUD
from connections import PostgresDatabaseConnection


router = APIRouter()
crud = DeliveryProviderCRUD()
conn = PostgresDatabaseConnection()

@router.post("/delivery_provider/create", response_model=int)
def create(data: DeliveryProviderData):
    """This service creates a new delivery provider in the database.
    Remember that the delivery provider data must have the specified structure."""
    print("Creating delivery provider", data)
    return crud.create(data)

@router.put("/delivery_provider/update/{id_}", response_model=bool)
def update(id_: int, data: DeliveryProviderData):
    """This service updates the delivery provider data in the database based on its id."""
    try:
        crud.update(id_, data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    

@router.delete("/delivery_provider/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a delivery provider from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    
    
@router.get("/delivery_provider/get_by_id/{id_}", response_model=Optional[DeliveryProviderData])
def get_by_id(id_: int):
    """This service gets a delivery provider from the database based on its id."""
    return crud.get_by_id(id_)


@router.get("/delivery_provider/get_all", response_model=List[DeliveryProviderData])
def get_all():
    """This service gets all the delivery providers from the database."""
    return crud.get_all()

@router.get("/delivery_provider/get_by_name/{name}", response_model=List[DeliveryProviderData])
def get_by_name(name: str):
    """This service gets a delivery provider from the database based on its name."""
    return crud.get_by_name(name)


@router.get("/delivery_provider/get_by_email/{email}", response_model=List[DeliveryProviderData])
def get_by_email(email: str):
    """This service gets a delivery provider from the database based on its email."""
    return crud.get_by_email(email)

@router.get("/delivery_provider/get_by_phone/{phone}", response_model=List[DeliveryProviderData])
def get_by_phone(phone: str):
    """This service gets a delivery provider from the database based on its phone."""
    return crud.get_by_phone(phone)

