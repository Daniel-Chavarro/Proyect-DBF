from connections import PostgresDatabaseConection as DatabaseConnection
from DAO import BrandData
from typing import List

class BrandCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, brand: BrandData) -> int:
        query = """
            INSERT INTO Brands (name, description)
            VALUES (%s, %s);
        """
        values = (brand.name, brand.description)
        return self._connection.create(query, values)
    
    def update(self, brand: BrandData):
        query = """
            UPDATE Brands
            SET name = %s, description = %s
            WHERE id_brand = %s;
        """
        values = (brand.name, brand.description, brand.id_brand)
        self._connection.update(query, values)
        
    def delete(self, brand_id: int):
        query = """
            DELETE FROM Brands
            WHERE id_brand = %s;
        """
        self._connection.delete(query, brand_id)
    
    def get_by_id(self, brand_id: int) -> BrandData:
        query = """
            SELECT * FROM Brands
            WHERE id_brand = %s;
        """
        values = (brand_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[BrandData]:
        query = """
            SELECT * FROM Brands;
        """
        return self._connection.get_many(query)
    
    def get_brand_with_product(self, brand_id: int) -> BrandData:
        query = """
            SELECT Brands.*, Product.name AS product_name, Product.description AS product_description
            FROM Brands
            JOIN Product ON Brands.id_brand = Product.id_brand_fk
            WHERE Brands.id_brand = %s;
        """
        values = (brand_id,)
        return self._connection.get_one(query, values)

    def get_by_name_and_description(self, name: str, description: str) -> List[BrandData]:
        query = """
            SELECT * FROM Brands
            WHERE name = %s AND description = %s;
        """
        values = (name, description)
        return self._connection.get_many(query, values)

    def get_by_name_and_id(self, name: str, brand_id: int) -> List[BrandData]:
        query = """
            SELECT * FROM Brands
            WHERE name = %s AND id_brand = %s;
        """
        values = (name, brand_id)
        return self._connection.get_many(query, values)
