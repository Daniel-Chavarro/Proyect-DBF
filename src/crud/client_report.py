from connections import DatabaseConnection
from DAO import ClientReportData
from typing import List

class ClientReportCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, report: ClientReportData) -> int:
        query = """
            INSERT INTO ClientReport (id_user_reporter_fk, id_user_reported_fk, id_category_report_fk, id_status_report_fk, description, date_created)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        values = (report.id_user_reporter_fk, report.id_user_reported_fk, report.id_category_report_fk, report.id_status_report_fk, report.description, report.date_created)
        return self._connection.create(query, values)
    
    def update(self, report: ClientReportData):
        query = """
            UPDATE ClientReport
            SET id_user_reporter_fk = %s, id_user_reported_fk = %s, id_category_report_fk = %s, id_status_report_fk = %s, description = %s, date_created = %s
            WHERE id_client_report = %s;
        """
        values = (report.id_user_reporter_fk, report.id_user_reported_fk, report.id_category_report_fk, report.id_status_report_fk, report.description, report.date_created, report.id_client_report)
        self._connection.update(query, values)
        
    def delete(self, report_id: int):
        query = """
            DELETE FROM ClientReport
            WHERE id_client_report = %s;
        """
        self._connection.delete(query, report_id)
    
    def get_by_id(self, report_id: int) -> ClientReportData:
        query = """
            SELECT * FROM ClientReport
            WHERE id_client_report = %s;
        """
        values = (report_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[ClientReportData]:
        query = """
            SELECT * FROM ClientReport;
        """
        return self._connection.get_many(query)
    
    def get_report_with_user(self, report_id: int) -> ClientReportData:
        query = """
            SELECT ClientReport.*, Users.name AS user_name, Users.email AS user_email
            FROM ClientReport
            JOIN Users ON ClientReport.id_user_reporter_fk = Users.id_user
            WHERE ClientReport.id_client_report = %s;
        """
        values = (report_id,)
        return self._connection.get_one(query, values)
    
    def get_report_with_category(self, report_id: int) -> ClientReportData:
        query = """
            SELECT ClientReport.*, CategoryReport.name AS category_name, CategoryReport.description AS category_description
            FROM ClientReport
            JOIN CategoryReport ON ClientReport.id_category_report_fk = CategoryReport.id_category_report
            WHERE ClientReport.id_client_report = %s;
        """
        values = (report_id,)
        return self._connection.get_one(query, values)
    
    def get_report_with_status(self, report_id: int) -> ClientReportData:
        query = """
            SELECT ClientReport.*, StatusReport.name AS status_name, StatusReport.description AS status_description
            FROM ClientReport
            JOIN StatusReport ON ClientReport.id_status_report_fk = StatusReport.id_status_report
            WHERE ClientReport.id_client_report = %s;
        """
        values = (report_id,)
        return self._connection.get_one(query, values)
    
    def get_by_user_and_category(self, user_id: int, category_id: int) -> List[ClientReportData]:
        query = """
            SELECT * FROM ClientReport
            WHERE id_user_reporter_fk = %s AND id_category_report_fk = %s;
        """
        values = (user_id, category_id)
        return self._connection.get_many(query, values)
    
    def get_by_user_and_status(self, user_id: int, status_id: int) -> List[ClientReportData]:
        query = """
            SELECT * FROM ClientReport
            WHERE id_user_reporter_fk = %s AND id_status_report_fk = %s;
        """
        values = (user_id, status_id)
        return self._connection.get_many(query, values)
    
    def get_by_category_and_status(self, category_id: int, status_id: int) -> List[ClientReportData]:
        query = """
            SELECT * FROM ClientReport
            WHERE id_category_report_fk = %s AND id_status_report_fk = %s;
        """
        values = (category_id, status_id)
        return self._connection.get_many(query, values)
