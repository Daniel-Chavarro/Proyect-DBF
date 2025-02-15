from DAO import ProductStatusData
from connections import DatabaseConnection
from typing import List

class ProductStatusCrud:
    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.db_connection.connect()
    
    def create(self, product_status: ProductStatusData) -> int:
        query = f"""
            INSERT INTO product_status (id_product_status ,name, description)
            VALUES ('%s', '%s', '%s')
        """
        
        values = (product_status.id_product_status, product_status.name, product_status.description)
        return self.db_connection.create(query, values)

    def update(self, product_status: ProductStatusData):
        query = f"""
            UPDATE product_status
            SET name = '%s', description = '%s'
            WHERE id_product_status = '%s'
        """
        values = (product_status.name, product_status.description, product_status.id_product_status)
        self.db_connection.update(query, values)
    
    def delete(self, product_status_id: int):
        query = f"""
            DELETE FROM product_status
            WHERE id_product_status = '%s'
        """
        values = (product_status_id,)
        self.db_connection.delete(query, values)
    
    def get_by_id(self, product_status_id: int) -> ProductStatusData:
        query = f"""
            SELECT * FROM product_status
            WHERE id_product_status = '%s'
        """
        values = (product_status_id,)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[ProductStatusData]:
        query = f"""
            SELECT * FROM product_status
        """
        return self.db_connection.get_many(query)

    def get_by_name(self, status_name: str) -> ProductStatusData:
        query = f"""
            SELECT * FROM product_status
            WHERE name LIKE = '%s'
        """
        values = (status_name,)
        return self.db_connection.get_one(query, values)