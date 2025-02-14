from connections import PostgresDatabaseConection as DatabaseConnection
from DAO import CategoryReportData
from typing import List

class CategoryReportCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, category: CategoryReportData) -> int:
        query = """
            INSERT INTO CategoryReport (name, description)
            VALUES (%s, %s);
        """
        values = (category.name, category.description)
        return self._connection.create(query, values)
    
    def update(self, category: CategoryReportData):
        query = """
            UPDATE CategoryReport
            SET name = %s, description = %s
            WHERE id_category_report = %s;
        """
        values = (category.name, category.description, category.id_category_report)
        self._connection.update(query, values)
        
    def delete(self, category_id: int):
        query = """
            DELETE FROM CategoryReport
            WHERE id_category_report = %s;
        """
        self._connection.delete(query, category_id)
    
    def get_by_id(self, category_id: int) -> CategoryReportData:
        query = """
            SELECT * FROM CategoryReport
            WHERE id_category_report = %s;
        """
        values = (category_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[CategoryReportData]:
        query = """
            SELECT * FROM CategoryReport;
        """
        return self._connection.get_many(query)
