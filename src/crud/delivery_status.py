from DAO import DeliveryStatusData
from connections import DatabaseConnection
from typing import List

class DeliveryStatusCrud:
    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.db_connection.connect()
    
    def create(self, delivery_status: DeliveryStatusData) -> int:
        query = """
            INSERT INTO delivery_status (name, description)
            VALUES (%s, %s)
        """
        values = (delivery_status.name, delivery_status.description)
        return self.db_connection.create(query, values)

    def update(self, delivery_status: DeliveryStatusData):
        query = """
            UPDATE delivery_status
            SET name = %s, description = %s
            WHERE id_delivery_status = %s
        """
        values = (delivery_status.name, delivery_status.description, delivery_status.id)
        self.db_connection.update(query, values)
    
    def delete(self, delivery_status_id: int):
        query = """
            DELETE FROM delivery_status
            WHERE id_delivery_status = %s
        """
        
        values = (delivery_status_id,)
        self.db_connection.delete(query, values)
    
    def get_by_id(self, delivery_status_id: int) -> DeliveryStatusData:
        query = """
            SELECT * FROM delivery_status
            WHERE id_delivery_status = %s
        """
        
        values = (delivery_status_id,)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[DeliveryStatusData]:
        query = """
            SELECT * FROM delivery_status
        """
        return self.db_connection.get_many(query)

    def get_by_status_name(self, status_name: str) -> DeliveryStatusData:
        query = """
            SELECT * FROM delivery_status
            WHERE name LIKE %s
        """
        values = (status_name,)
        return self.db_connection.get_one(query, values)