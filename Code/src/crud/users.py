from database_conection import PostgresDatabaseConection

class UsersCRUD():
    
    def __init__(self):
        self._connection = PostgresDatabaseConection()
        self._connection.connect()