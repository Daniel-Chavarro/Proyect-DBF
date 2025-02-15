from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import ReceiptData
from crud import ReceiptCrud
from connections import PostgresDatabaseConnection

router = APIRouter()
crud = ReceiptCrud()
conn = PostgresDatabaseConnection()

@router.post("/receipt/create", response_model=int)
def create(data: ReceiptData):
    """This service creates a new receipt in the database."""
    print("Creating receipt", data)
    return crud.create(data)

@router.put("/receipt/update/{id_}", response_model=bool)
def update(id_: int, data: ReceiptData):
    """This service updates the receipt data in the database based on its id."""
    try:
        crud.update(data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.delete("/receipt/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a receipt from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/receipt/get_by_id/{id_}", response_model=Optional[ReceiptData])
def get_by_id(id_: int):
    """This service gets a receipt from the database based on its id."""
    return crud.get_by_id(id_)

@router.get("/receipt/get_all", response_model=List[ReceiptData])
def get_all():
    """This service gets all the receipts from the database."""
    return crud.get_all()