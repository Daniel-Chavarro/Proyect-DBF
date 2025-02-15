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
        values = (brand_id,)
        self._connection.delete(query, values)
    
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


    def get_by_name(self, name: str) -> List[BrandData]:
        query = """
            SELECT * FROM Brands
            WHERE name = %s;
        """
        values = (name,)
        return self._connection.get_many(query, values)