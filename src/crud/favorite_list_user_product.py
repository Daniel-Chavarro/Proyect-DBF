from connections import PostgresDatabaseConection as DatabaseConnection
from DAO import FavoriteListUserProductData
from typing import List

class FavoriteListUserProductCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, favorite: FavoriteListUserProductData) -> int:
        query = """
            INSERT INTO FavoriteListUsersProduct (id_user_fk, id_product_fk, date_added, name)
            VALUES (%s, %s, %s, %s);
        """
        values = (favorite.id_user_fk, favorite.id_product_fk, favorite.date_added, favorite.name)
        return self._connection.create(query, values)
    
    def update(self, favorite: FavoriteListUserProductData):
        query = """
            UPDATE FavoriteListUsersProduct
            SET id_user_fk = %s, id_product_fk = %s, date_added = %s, name = %s
            WHERE id_favorite_product = %s;
        """
        values = (favorite.id_user_fk, favorite.id_product_fk, favorite.date_added, favorite.name, favorite.id_favorite_product)
        self._connection.update(query, values)
        
    def delete(self, favorite_id: int):
        query = """
            DELETE FROM FavoriteListUsersProduct
            WHERE id_favorite_product = %s;
        """
        values = (favorite_id,)
        self._connection.delete(query, values)
    
    def get_by_id(self, favorite_id: int) -> FavoriteListUserProductData:
        query = """
            SELECT * FROM FavoriteListUsersProduct
            WHERE id_favorite_product = %s;
        """
        values = (favorite_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[FavoriteListUserProductData]:
        query = """
            SELECT * FROM FavoriteListUsersProduct;
        """
        return self._connection.get_many(query)
