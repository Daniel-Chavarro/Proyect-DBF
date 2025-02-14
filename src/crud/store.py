from connections import PostgresDatabaseConection as DatabaseConnection
from DAO import StoreData
from typing import List

class StoreCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, store: StoreData) -> int:
        query = """
            INSERT INTO Store (id_user_fk, id_address_fk, name, description, phone, email, date_created)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        values = (store.id_user_fk, store.id_address_fk, store.name, store.description, store.phone, store.email, store.date_created)
        return self._connection.create(query, values)
    
    def update(self, store: StoreData):
        query = """
            UPDATE Store
            SET id_address_fk = %s, name = %s, description = %s, phone = %s, email = %s
            WHERE id_store = %s;
        """
        values = (store.id_address_fk, store.name, store.description, store.phone, store.email, store.id_store)
        self._connection.update(query, values)
        
    def delete(self, store_id: int):
        query = """
            DELETE FROM Store
            WHERE id_store = %s;
        """
        self._connection.delete(query, store_id)
    
    def get_by_id(self, store_id: int) -> StoreData:
        query = """
            SELECT * FROM Store
            WHERE id_store = %s;
        """
        values = (store_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[StoreData]:
        query = """
            SELECT * FROM Store;
        """
        return self._connection.get_many(query)
    
    def get_by_user_id(self, user_id: int) -> List[StoreData]:
        query = """
            SELECT * FROM Store
            WHERE id_user_fk = %s;
        """
        values = (user_id,)
        return self._connection.get_many(query, values)

    def get_by_address_id(self, address_id: int) -> List[StoreData]:
        query = """
            SELECT * FROM Store
            WHERE id_address_fk = %s;
        """
        values = (address_id,)
        return self._connection.get_many(query, values)

    def get_store_with_address(self, store_id: int) -> StoreData:
            query = """
                SELECT Store.*, Address.*
                FROM Store
                JOIN Address ON Store.id_address_fk = Address.id_address
                WHERE Store.id_store = %s;
            """
            values = (store_id,)
            return self._connection.get_one(query, values)