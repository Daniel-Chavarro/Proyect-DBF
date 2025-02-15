from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import PaymentMethodData
from crud import PaymentMethodCrud
from connections import PostgresDatabaseConnection

router = APIRouter()
crud = PaymentMethodCrud()
conn = PostgresDatabaseConnection()

@router.post("/payment_method/create", response_model=int)
def create(data: PaymentMethodData):
    """This service creates a new payment method in the database."""
    print("Creating payment method", data)
    return crud.create(data)

@router.put("/payment_method/update/{id_}", response_model=bool)
def update(id_: int, data: PaymentMethodData):
    """This service updates the payment method data in the database based on its id."""
    try:
        crud.update(data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.delete("/payment_method/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a payment method from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/payment_method/get_by_id/{id_}", response_model=Optional[PaymentMethodData])
def get_by_id(id_: int):
    """This service gets a payment method from the database based on its id."""
    return crud.get_by_id(id_)

@router.get("/payment_method/get_all", response_model=List[PaymentMethodData])
def get_all():
    """This service gets all the payment methods from the database."""
    return crud.get_all()