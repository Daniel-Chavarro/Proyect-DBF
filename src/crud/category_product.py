from connections import DatabaseConnection
from DAO import CategoryProductData
from typing import List

class CategoryProductCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, category: CategoryProductData) -> int:
        query = """
            INSERT INTO CategoryProduct (name, description)
            VALUES (%s, %s);
        """
        values = (category.name, category.description)
        return self._connection.create(query, values)
    
    def update(self, category: CategoryProductData):
        query = """
            UPDATE CategoryProduct
            SET name = %s, description = %s
            WHERE id_category = %s;
        """
        values = (category.name, category.description, category.id_category)
        self._connection.update(query, values)
        
    def delete(self, category_id: int):
        query = """
            DELETE FROM CategoryProduct
            WHERE id_category = %s;
        """
        self._connection.delete(query, category_id)
    
    def get_by_id(self, category_id: int) -> CategoryProductData:
        query = """
            SELECT * FROM CategoryProduct
            WHERE id_category = %s;
        """
        values = (category_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[CategoryProductData]:
        query = """
            SELECT * FROM CategoryProduct;
        """
        return self._connection.get_many(query)

    def get_by_name(self, name: str) -> List[CategoryProductData]:
        query = """
            SELECT * FROM CategoryProduct
            WHERE name = %s;
        """
        values = (name,)
        return self._connection.get_many(query, values)
    

