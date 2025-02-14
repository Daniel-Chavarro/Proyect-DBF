from DAO import StatusReportData
from connections import DatabaseConnection
from typing import List

class StatusReportCrud:
    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.db_connection.connect()
    
    def create(self, status_report: StatusReportData) -> int:
        query = """
            INSERT INTO status_report (name, description)
            VALUES (%s, %s)
        """
        values = (status_report.name, status_report.description)
        return self.db_connection.create(query, values)

    def update(self, status_report: StatusReportData):
        query = """
            UPDATE status_report
            SET name = %s, description = %s
            WHERE id_status_report = %s
        """
        values = (status_report.name, status_report.description, status_report.id)
        self.db_connection.update(query, values)
    
    def delete(self, status_report_id: int):
        query = """
            DELETE FROM status_report
            WHERE id_status_report = %s
        """
        self.db_connection.delete(query, status_report_id)
    
    def get_by_id(self, status_report_id: int) -> StatusReportData:
        query = """
            SELECT * FROM status_report
            WHERE id_status_report = %s
        """
        return self.db_connection.get_one(query, status_report_id)

    def get_all(self) -> List[StatusReportData]:
        query = """
            SELECT * FROM status_report
        """
        return self.db_connection.get_many(query)

    def get_by_status_name(self, status_name: str) -> StatusReportData:
        query = """
            SELECT * FROM status_report
            WHERE name LIKE %s
        """
        return self.db_connection.get_one(query, status_name)