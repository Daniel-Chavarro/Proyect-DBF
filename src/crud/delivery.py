from connections import PostgresDatabaseConection as DatabaseConnection
from DAO import DeliveryData
from typing import List

class DeliveryCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, delivery: DeliveryData) -> int:
        query = """
            INSERT INTO Delivery (id_user_fk, id_shopping_cart_fk, id_delivery_provider_fk, id_delivery_status_fk, id_address_fk, date_created, date_estimated_arrive, delivery_cost)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        values = (delivery.id_user_fk, delivery.id_shopping_cart_fk, delivery.id_delivery_provider_fk, delivery.id_delivery_status_fk, delivery.id_address_fk, delivery.date_created, delivery.date_estimated_arrive, delivery.delivery_cost)
        return self._connection.create(query, values)
    
    def update(self, delivery: DeliveryData):
        query = """
            UPDATE Delivery
            SET id_user_fk = %s, id_shopping_cart_fk = %s, id_delivery_provider_fk = %s, id_delivery_status_fk = %s, id_address_fk = %s, date_created = %s, date_estimated_arrive = %s, delivery_cost = %s
            WHERE id_delivery = %s;
        """
        values = (delivery.id_user_fk, delivery.id_shopping_cart_fk, delivery.id_delivery_provider_fk, delivery.id_delivery_status_fk, delivery.id_address_fk, delivery.date_created, delivery.date_estimated_arrive, delivery.delivery_cost, delivery.id_delivery)
        self._connection.update(query, values)
        
    def delete(self, delivery_id: int):
        query = """
            DELETE FROM Delivery
            WHERE id_delivery = %s;
        """
        values = (delivery_id,)
        self._connection.delete(query, values)
    
    def get_by_id(self, delivery_id: int) -> DeliveryData:
        query = """
            SELECT * FROM Delivery
            WHERE id_delivery = %s;
        """
        values = (delivery_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[DeliveryData]:
        query = """
            SELECT * FROM Delivery;
        """
        return self._connection.get_many(query)

    def get_by_user_id(self, user_id: int) -> List[DeliveryData]:
        query = """
            SELECT * FROM Delivery
            WHERE id_user_fk = %s;
        """
        values = (user_id,)
        return self._connection.get_many(query, values)

    def get_by_status_id(self, status_id: int) -> List[DeliveryData]:
        query = """
            SELECT * FROM Delivery
            WHERE id_delivery_status_fk = %s;
        """
        values = (status_id,)
        return self._connection.get_many(query, values)

    def get_by_provider_id(self, provider_id: int) -> List[DeliveryData]:
        query = """
            SELECT * FROM Delivery
            WHERE id_delivery_provider_fk = %s;
        """
        values = (provider_id,)
        return self._connection.get_many(query, values)

    def get_delivery_with_user(self, delivery_id: int) -> DeliveryData:
        query = """
            SELECT Delivery.*, Users.name AS user_name, Users.email AS user_email
            FROM Delivery
            JOIN Users ON Delivery.id_user_fk = Users.id_user
            WHERE Delivery.id_delivery = %s;
        """
        values = (delivery_id,)
        return self._connection.get_one(query, values)

    def get_delivery_with_status(self, delivery_id: int) -> DeliveryData:
        query = """
            SELECT Delivery.*, DeliveryStatus.name AS status_name, DeliveryStatus.description AS status_description
            FROM Delivery
            JOIN DeliveryStatus ON Delivery.id_delivery_status_fk = DeliveryStatus.id_delivery_status
            WHERE Delivery.id_delivery = %s;
        """
        values = (delivery_id,)
        return self._connection.get_one(query, values)

    def get_by_user_and_status(self, user_id: int, status_id: int) -> List[DeliveryData]:
        query = """
            SELECT * FROM Delivery
            WHERE id_user_fk = %s AND id_delivery_status_fk = %s;
        """
        values = (user_id, status_id)
        return self._connection.get_many(query, values)

    def get_by_provider_and_status(self, provider_id: int, status_id: int) -> List[DeliveryData]:
        query = """
            SELECT * FROM Delivery
            WHERE id_delivery_provider_fk = %s AND id_delivery_status_fk = %s;
        """
        values = (provider_id, status_id)
        return self._connection.get_many(query, values)
