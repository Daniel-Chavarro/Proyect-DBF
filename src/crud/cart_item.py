from connections import PostgresDatabaseConection as DatabaseConnection
from DAO import CartItemData
from typing import List

class CartItemCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, item: CartItemData) -> int:
        query = """
            INSERT INTO CartItems (id_shopping_cart_fk, id_product_fk, quantity, subtotal)
            VALUES (%s, %s, %s, %s);
        """
        values = (item.id_shopping_cart_fk, item.id_product_fk, item.quantity, item.subtotal)
        return self._connection.create(query, values)
    
    def update(self, item: CartItemData):
        query = """
            UPDATE CartItems
            SET id_shopping_cart_fk = %s, id_product_fk = %s, quantity = %s, subtotal = %s
            WHERE id_cart_item = %s;
        """
        values = (item.id_shopping_cart_fk, item.id_product_fk, item.quantity, item.subtotal, item.id_cart_item)
        self._connection.update(query, values)
        
    def delete(self, item_id: int):
        query = """
            DELETE FROM CartItems
            WHERE id_cart_item = %s;
        """
        self._connection.delete(query, item_id)
    
    def get_by_id(self, item_id: int) -> CartItemData:
        query = """
            SELECT * FROM CartItems
            WHERE id_cart_item = %s;
        """
        values = (item_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[CartItemData]:
        query = """
            SELECT * FROM CartItems;
        """
        return self._connection.get_many(query)
    
    def get_by_shopping_cart_id(self, cart_id: int) -> List[CartItemData]:
        query = """
            SELECT * FROM CartItems
            WHERE id_shopping_cart_fk = %s;
        """
        values = (cart_id,)
        return self._connection.get_many(query, values)

    def get_item_with_product(self, item_id: int) -> CartItemData:
        query = """
            SELECT CartItems.*, Product.name AS product_name, Product.description AS product_description
            FROM CartItems
            JOIN Product ON CartItems.id_product_fk = Product.id_product
            WHERE CartItems.id_cart_item = %s;
        """
        values = (item_id,)
        return self._connection.get_one(query, values)

    def get_item_with_cart(self, item_id: int) -> CartItemData:
        query = """
            SELECT CartItems.*, ShoppingCart.total AS cart_total, ShoppingCart.date_created AS cart_date_created
            FROM CartItems
            JOIN ShoppingCart ON CartItems.id_shopping_cart_fk = ShoppingCart.id_shopping_cart
            WHERE CartItems.id_cart_item = %s;
        """
        values = (item_id,)
        return self._connection.get_one(query, values)
