from DAO import TransactionStatusData
from connections import DatabaseConnection
from typing import List

class TransactionStatusCrud:
    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.db_connection.connect()
    
    def create(self, transaction_status: TransactionStatusData) -> int:
        query = """
            INSERT INTO transaction_status (name, description)
            VALUES (%s, %s)
        """
        values = (transaction_status.name, transaction_status.description)
        return self.db_connection.create(query, values)

    def update(self, transaction_status: TransactionStatusData):
        query = """
            UPDATE transaction_status
            SET name = %s, description = %s
            WHERE id_transaction_status = %s
        """
        values = (transaction_status.name, transaction_status.description, transaction_status.id)
        self.db_connection.update(query, values)
    
    def delete(self, transaction_status_id: int):
        query = """
            DELETE FROM transaction_status
            WHERE id_transaction_status = %s
        """
        values = (transaction_status_id,)
        self.db_connection.delete(query, values)
    
    def get_by_id(self, transaction_status_id: int) -> TransactionStatusData:
        query = """
            SELECT * FROM transaction_status
            WHERE id_transaction_status = %s
        """
        values = (transaction_status_id,)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[TransactionStatusData]:
        query = """
            SELECT * FROM transaction_status
        """
        return self.db_connection.get_many(query)

    def get_by_status_name(self, status_name: str) -> TransactionStatusData:
        query = """
            SELECT * FROM transaction_status
            WHERE name LIKE %s
        """
        values = (status_name,)
        return self.db_connection.get_one(query, values)