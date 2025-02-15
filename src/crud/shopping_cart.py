from connections import DatabaseConnection
from DAO import ShoppingCartData
from typing import List

class ShoppingCartCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, cart: ShoppingCartData) -> int:
        query = """
            INSERT INTO ShoppingCart (id_status_cart_fk, id_user_fk, date_created, total)
            VALUES (%s, %s, %s, %s);
        """
        values = (cart.id_status_cart_fk, cart.id_user_fk, cart.date_created, cart.total)
        return self._connection.create(query, values)
    
    def update(self, cart: ShoppingCartData):
        query = """
            UPDATE ShoppingCart
            SET id_status_cart_fk = %s, date_created = %s, total = %s
            WHERE id_shopping_cart = %s;
        """
        values = (cart.id_status_cart_fk, cart.date_created, cart.total, cart.id_shopping_cart)
        self._connection.update(query, values)
        
    def delete(self, cart_id: int):
        query = """
            DELETE FROM ShoppingCart
            WHERE id_shopping_cart = %s;
        """
        values = (cart_id,)
        self._connection.delete(query, values)
    
    def get_by_id(self, cart_id: int) -> ShoppingCartData:
        query = """
            SELECT * FROM ShoppingCart
            WHERE id_shopping_cart = %s;
        """
        values = (cart_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[ShoppingCartData]:
        query = """
            SELECT * FROM ShoppingCart;
        """
        return self._connection.get_many(query)

    def get_cart_with_user(self, cart_id: int) -> ShoppingCartData:
        query = """
            SELECT ShoppingCart.*, Users.name AS user_name, Users.email AS user_email
            FROM ShoppingCart
            JOIN Users ON ShoppingCart.id_user_fk = Users.id_user
            WHERE ShoppingCart.id_shopping_cart = %s;
        """
        values = (cart_id,)
        return self._connection.get_one(query, values)

    def get_cart_with_status(self, cart_id: int) -> ShoppingCartData:
        query = """
            SELECT ShoppingCart.*, StatusCart.name AS status_name, StatusCart.description AS status_description
            FROM ShoppingCart
            JOIN StatusCart ON ShoppingCart.id_status_cart_fk = StatusCart.id_status_cart
            WHERE ShoppingCart.id_shopping_cart = %s;
        """
        values = (cart_id,)
        return self._connection.get_one(query, values)

    def get_by_user_and_status(self, user_id: int, status_id: int) -> List[ShoppingCartData]:
        query = """
            SELECT * FROM ShoppingCart
            WHERE id_user_fk = %s AND id_status_cart_fk = %s;
        """
        values = (user_id, status_id)
        return self._connection.get_many(query, values)

    def get_by_date_and_total(self, date_created: str, total: float) -> List[ShoppingCartData]:
        query = """
            SELECT * FROM ShoppingCart
            WHERE date_created = %s AND total = %s;
        """
        values = (date_created, total)
        return self._connection.get_many(query, values)
    
    def get_by_user_id(self, user_id: int) -> List[ShoppingCartData]:
        query = """
            SELECT * FROM ShoppingCart
            WHERE id_user_fk = %s;
        """
        values = (user_id,)
        return self._connection.get_many(query, values)
    
    def get_by_status_id(self, status_id: int) -> List[ShoppingCartData]:
        query = """
            SELECT * FROM ShoppingCart
            WHERE id_status_cart_fk = %s;
        """
        values = (status_id,)
        return self._connection.get_many(query, values)
    
    def get_by_total(self, total: float) -> List[ShoppingCartData]:
        query = """
            SELECT * FROM ShoppingCart
            WHERE total = %s;
        """
        values = (total,)
        return self._connection.get_many(query, values)
    
    def get_by_user_and_date(self, user_id: int, date_created: str) -> List[ShoppingCartData]:
        query = """
            SELECT * FROM ShoppingCart
            WHERE id_user_fk = %s AND date_created = %s;
        """
        values = (user_id, date_created)
        return self._connection.get_many(query, values)
    
    def get_by_status_and_total(self, status_id: int, total: float) -> List[ShoppingCartData]:
        query = """
            SELECT * FROM ShoppingCart
            WHERE id_status_cart_fk = %s AND total = %s;
        """
        values = (status_id, total)
        return self._connection.get_many(query, values)
