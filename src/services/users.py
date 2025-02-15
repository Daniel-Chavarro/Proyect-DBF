from typing import List, Optional
from fastapi import HTTPException, APIRouter

from DAO import UserData
from crud import UsersCRUD
from connections import DatabaseConnection


router = APIRouter()
crud = UsersCRUD()
conn = DatabaseConnection()

@router.post("/user/create/", response_model=int)
def create(data: UserData):
    print(conn.list_schemas())
    """This service creates a new user in the database.
    Remember that the user data must have the specified struture."""
    print("Creating user", data)
    return crud.create(data)

@router.put("/user/update/{id_}", response_model=bool)
def update(id_: int, data: UserData):
    """This service updates the user data in the database based on its id."""
    try:
        crud.update(id_, data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e


@router.delete("/user/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a user from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/user/get_by_id/{id_}", response_model=Optional[UserData])
def get_by_id(id_: int):
    """This service gets a user from the database based on its id."""
    return crud.get_by_id(id_)


@router.get("/user/get_all", response_model=List[UserData])
def get_all():
    """This service gets all the users from the database."""
    return crud.get_all()

@router.get("/user/get_by_username/{username}", response_model=Optional[UserData])
def get_by_username(username: str):
    """This service gets a user from the database based on its username."""
    return crud.get_by_username(username)

@router.get("/user/get_by_name/{name}", response_model=List[UserData])
def get_by_name(name: str):
    """This service gets a user from the database based on its name."""
    return crud.get_by_name(name)


@router.get("/user/get_by_email/{email}", response_model=Optional[UserData])
def get_by_email(email: str):
    """This service gets a user from the database based on its email."""
    return crud.get_by_email(email)

@router.get("/user/get_by_phone/{phone}", response_model=Optional[UserData])
def get_by_phone(phone: str):
    """This service gets a user from the database based on its phone."""
    return crud.get_by_phone(phone)

@router.get("/user/get_by_last_name/{last_name}", response_model=List[UserData])
def get_by_last_name(last_name: str):
    """This service gets users from the database based on their last name."""
    return crud.get_by_last_name(last_name)

@router.get("/user/get_by_role/{role}", response_model=List[UserData])
def get_by_role(role: str):
    """This service gets users from the database based on their role."""
    return crud.get_by_role(role)

@router.get("/user/get_by_id_status/{id_status}", response_model=List[UserData])
def get_by_id_status(id_status: int):
    """This service gets users from the database based on their account status id."""
    return crud.get_by_id_status(id_status)

@router.get("/user/get_by_id_type_user/{type_user}", response_model=List[UserData])
def get_by_id_type_user(type_user: int):
    """This service gets users from the database based on their type user id."""
    return crud.get_by_id_type_user(type_user)

@router.get("/user/get_user_with_address/{id_user}", response_model=Optional[UserData])
def get_user_with_address(id_user: int):
    """This service gets a user with their address from the database based on their id."""
    return crud.get_user_with_address(id_user)

@router.get("/user/get_all_users_with_address", response_model=List[UserData])
def get_all_users_with_address():
    """This service gets all users with their addresses from the database."""
    return crud.get_all_users_with_address()

@router.get("/user/validate_seller/{id_user}", response_model=bool)
def validate_seller(id_user: int):
    """This service validates if a user is a seller based on their id."""
    return crud.validate_seller(id_user)


