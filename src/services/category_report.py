from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import CategoryReportData
from crud import CategoryReportCRUD
from connections import DatabaseConnection

router = APIRouter()
crud = CategoryReportCRUD()
conn = DatabaseConnection()

@router.post("/category_report/create", response_model=int)
def create(data: CategoryReportData):
    """This service creates a new category report in the database."""
    print("Creating category report", data)
    return crud.create(data)

@router.put("/category_report/update/{id_}", response_model=bool)
def update(id_: int, data: CategoryReportData):
    """This service updates the category report data in the database based on its id."""
    try:
        crud.update(data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.delete("/category_report/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a category report from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/category_report/get_by_id/{id_}", response_model=Optional[CategoryReportData])
def get_by_id(id_: int):
    """This service gets a category report from the database based on its id."""
    return crud.get_by_id(id_)

@router.get("/category_report/get_all", response_model=List[CategoryReportData])
def get_all():
    """This service gets all the category reports from the database."""
    return crud.get_all()