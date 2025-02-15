from DAO import StatusCartData
from connections import DatabaseConnection
from typing import List

class StatusCartCrud:
    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.db_connection.connect()
    
    def create(self, status_cart: StatusCartData) -> int:
        query = """
            INSERT INTO status_cart (name, description)
            VALUES (%s, %s)
        """
        values = (status_cart.name, status_cart.description)
        return self.db_connection.create(query, values)

    def update(self, status_cart: StatusCartData):
        query = """
            UPDATE status_cart
            SET name = %s, description = %s
            WHERE id_status_cart = %s
        """
        values = (status_cart.name, status_cart.description, status_cart.id)
        self.db_connection.update(query, values)
    
    def delete(self, status_cart_id: int):
        query = """
            DELETE FROM status_cart
            WHERE id_status_cart = %s
        """
        values = (status_cart_id,)
        self.db_connection.delete(query, values)
    
    def get_by_id(self, status_cart_id: int) -> StatusCartData:
        query = """
            SELECT * FROM status_cart
            WHERE id_status_cart = %s
        """
        values = (status_cart_id,)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[StatusCartData]:
        query = """
            SELECT * FROM status_cart
        """
        return self.db_connection.get_many(query)

    def get_by_status_name(self, status_name: str) -> StatusCartData:
        query = """
            SELECT * FROM status_cart
            WHERE LOWER(name) LIKE LOWER(%s)
        """
        values = (status_name,)
        return self.db_connection.get_one(query, values)