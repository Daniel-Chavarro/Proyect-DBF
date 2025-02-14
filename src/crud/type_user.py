from connections import PostgresDatabaseConection as DatabaseConnection
from DAO import TypeUserData
from typing import List

class TypeUserCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, type_user: TypeUserData) -> int:
        query = """
            INSERT INTO TypeUsers (name, description)
            VALUES (%s, %s);
        """
        values = (type_user.name, type_user.description)
        return self._connection.create(query, values)
    
    def update(self, type_user: TypeUserData):
        query = """
            UPDATE TypeUsers
            SET name = %s, description = %s
            WHERE id_type_user = %s;
        """
        values = (type_user.name, type_user.description, type_user.id_type_user)
        self._connection.update(query, values)
        
    def delete(self, type_user_id: int):
        query = """
            DELETE FROM TypeUsers
            WHERE id_type_user = %s;
        """
        self._connection.delete(query, type_user_id)
    
    def get_by_id(self, type_user_id: int) -> TypeUserData:
        query = """
            SELECT * FROM TypeUsers
            WHERE id_type_user = %s;
        """
        values = (type_user_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[TypeUserData]:
        query = """
            SELECT * FROM TypeUsers;
        """
        return self._connection.get_many(query)
