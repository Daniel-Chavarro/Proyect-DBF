from connections import PostgresDatabaseConection as DatabaseConnection
from DAO import AccountStatusData
from typing import List

class AccountStatusCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, status: AccountStatusData) -> int:
        query = """
            INSERT INTO AccountStatus (name, description)
            VALUES (%s, %s);
        """
        values = (status.name, status.description)
        return self._connection.create(query, values)
    
    def update(self, status: AccountStatusData):
        query = """
            UPDATE AccountStatus
            SET name = %s, description = %s
            WHERE id_account_status = %s;
        """
        values = (status.name, status.description, status.id_account_status)
        self._connection.update(query, values)
        
    def delete(self, status_id: int):
        query = """
            DELETE FROM AccountStatus
            WHERE id_account_status = %s;
        """
        self._connection.delete(query, status_id)
    
    def get_by_id(self, status_id: int) -> AccountStatusData:
        query = """
            SELECT * FROM AccountStatus
            WHERE id_account_status = %s;
        """
        values = (status_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[AccountStatusData]:
        query = """
            SELECT * FROM AccountStatus;
        """
        return self._connection.get_many(query)