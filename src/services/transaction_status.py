from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import TransactionStatusData
from crud import TransactionStatusCrud
from connections import PostgresDatabaseConnection

router = APIRouter()
crud = TransactionStatusCrud()
conn = PostgresDatabaseConnection()

@router.post("/transaction_status/create", response_model=int)
def create(data: TransactionStatusData):
    """This service creates a new transaction status in the database."""
    print("Creating transaction status", data)
    return crud.create(data)

@router.put("/transaction_status/update/{id_}", response_model=bool)
def update(id_: int, data: TransactionStatusData):
    """This service updates the transaction status data in the database based on its id."""
    try:
        crud.update(data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.delete("/transaction_status/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a transaction status from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/transaction_status/get_by_id/{id_}", response_model=Optional[TransactionStatusData])
def get_by_id(id_: int):
    """This service gets a transaction status from the database based on its id."""
    return crud.get_by_id(id_)

@router.get("/transaction_status/get_all", response_model=List[TransactionStatusData])
def get_all():
    """This service gets all the transaction statuses from the database."""
    return crud.get_all()