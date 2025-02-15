from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import CategoryProductData
from crud import CategoryProductCRUD
from connections import DatabaseConnection


router = APIRouter()
crud = CategoryProductCRUD()
conn = DatabaseConnection()

@router.post("/category_product/create", response_model=int)
def create(data: CategoryProductData):
    """This service creates a new category product in the database.
    Remember that the category product data must have the specified structure."""
    print("Creating category product", data)
    return crud.create(data)

@router.put("/category_product/update/{id_}", response_model=bool)
def update(id_: int, data: CategoryProductData):
    """This service updates the category product data in the database based on its id."""
    try:
        crud.update(id_, data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    

@router.delete("/category_product/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a category product from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    
    
@router.get("/category_product/get_by_id/{id_}", response_model=Optional[CategoryProductData])
def get_by_id(id_: int):
    """This service gets a category product from the database based on its id."""
    return crud.get_by_id(id_)


@router.get("/category_product/get_all", response_model=List[CategoryProductData])
def get_all():
    """This service gets all the category products from the database."""
    return crud.get_all()

@router.get("/category_product/get_by_name/{name}", response_model=Optional[CategoryProductData])
def get_by_name(name: str):
    """This service gets a category product from the database based on its name."""
    return crud.get_by_name(name)
