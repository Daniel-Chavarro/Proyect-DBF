from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import StatusReportData
from crud import StatusReportCrud
from connections import DatabaseConnection

router = APIRouter()
crud = StatusReportCrud()
conn = DatabaseConnection()

@router.post("/status_report/create", response_model=int)
def create(data: StatusReportData):
    """This service creates a new status report in the database."""
    print("Creating status report", data)
    return crud.create(data)

@router.put("/status_report/update/{id_}", response_model=bool)
def update(id_: int, data: StatusReportData):
    """This service updates the status report data in the database based on its id."""
    try:
        crud.update(data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.delete("/status_report/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a status report from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/status_report/get_by_id/{id_}", response_model=Optional[StatusReportData])
def get_by_id(id_: int):
    """This service gets a status report from the database based on its id."""
    return crud.get_by_id(id_)

@router.get("/status_report/get_all", response_model=List[StatusReportData])
def get_all():
    """This service gets all the status reports from the database."""
    return crud.get_all()