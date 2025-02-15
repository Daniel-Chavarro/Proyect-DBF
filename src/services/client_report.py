from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import ClientReportData
from crud import ClientReportCrud
from connections import PostgresDatabaseConnection

router = APIRouter()
crud = ClientReportCrud()
conn = PostgresDatabaseConnection()

@router.post("/client_report/create", response_model=int)
def create(data: ClientReportData):
    """This service creates a new client report in the database."""
    print("Creating client report", data)
    return crud.create(data)

@router.put("/client_report/update/{id_}", response_model=bool)
def update(id_: int, data: ClientReportData):
    """This service updates the client report data in the database based on its id."""
    try:
        crud.update(data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.delete("/client_report/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a client report from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/client_report/get_by_id/{id_}", response_model=Optional[ClientReportData])
def get_by_id(id_: int):
    """This service gets a client report from the database based on its id."""
    return crud.get_by_id(id_)

@router.get("/client_report/get_all", response_model=List[ClientReportData])
def get_all():
    """This service gets all the client reports from the database."""
    return crud.get_all()