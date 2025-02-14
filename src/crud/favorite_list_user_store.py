from connections import PostgresDatabaseConection as DatabaseConnection
from DAO import FavoriteListUserStoreData
from typing import List

class FavoriteListUserStoreCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, favorite: FavoriteListUserStoreData) -> int:
        query = """
            INSERT INTO FavoriteListUsersStore (id_user_fk, id_store_fk, date_added, name)
            VALUES (%s, %s, %s, %s);
        """
        values = (favorite.id_user_fk, favorite.id_store_fk, favorite.date_added, favorite.name)
        return self._connection.create(query, values)
    
    def update(self, favorite: FavoriteListUserStoreData):
        query = """
            UPDATE FavoriteListUsersStore
            SET id_user_fk = %s, id_store_fk = %s, date_added = %s, name = %s
            WHERE id_favorite_store = %s;
        """
        values = (favorite.id_user_fk, favorite.id_store_fk, favorite.date_added, favorite.name, favorite.id_favorite_store)
        self._connection.update(query, values)
        
    def delete(self, favorite_id: int):
        query = """
            DELETE FROM FavoriteListUsersStore
            WHERE id_favorite_store = %s;
        """
        self._connection.delete(query, favorite_id)
    
    def get_by_id(self, favorite_id: int) -> FavoriteListUserStoreData:
        query = """
            SELECT * FROM FavoriteListUsersStore
            WHERE id_favorite_store = %s;
        """
        values = (favorite_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[FavoriteListUserStoreData]:
        query = """
            SELECT * FROM FavoriteListUsersStore;
        """
        return self._connection.get_many(query)
