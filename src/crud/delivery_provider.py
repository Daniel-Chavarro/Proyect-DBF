from connections import PostgresDatabaseConection as DatabaseConnection
from DAO import DeliveryProviderData
from typing import List

class DeliveryProviderCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, provider: DeliveryProviderData) -> int:
        query = """
            INSERT INTO DeliveryProvider (name, phone, email, description)
            VALUES (%s, %s, %s, %s);
        """
        values = (provider.name, provider.phone, provider.email, provider.description)
        return self._connection.create(query, values)
    
    def update(self, provider: DeliveryProviderData):
        query = """
            UPDATE DeliveryProvider
            SET name = %s, phone = %s, email = %s, description = %s
            WHERE id_delivery_provider = %s;
        """
        values = (provider.name, provider.phone, provider.email, provider.description, provider.id_delivery_provider)
        self._connection.update(query, values)
        
    def delete(self, provider_id: int):
        query = """
            DELETE FROM DeliveryProvider
            WHERE id_delivery_provider = %s;
        """
        self._connection.delete(query, provider_id)
    
    def get_by_id(self, provider_id: int) -> DeliveryProviderData:
        query = """
            SELECT * FROM DeliveryProvider
            WHERE id_delivery_provider = %s;
        """
        values = (provider_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[DeliveryProviderData]:
        query = """
            SELECT * FROM DeliveryProvider;
        """
        return self._connection.get_many(query)
    
    def get_provider_with_delivery(self, provider_id: int) -> DeliveryProviderData:
        query = """
            SELECT DeliveryProvider.*, Delivery.date_created AS delivery_date_created, Delivery.date_estimated_arrive AS delivery_date_estimated_arrive
            FROM DeliveryProvider
            JOIN Delivery ON DeliveryProvider.id_delivery_provider = Delivery.id_delivery_provider_fk
            WHERE DeliveryProvider.id_delivery_provider = %s;
        """
        values = (provider_id,)
        return self._connection.get_one(query, values)

    def get_by_name_and_phone(self, name: str, phone: str) -> List[DeliveryProviderData]:
        query = """
            SELECT * FROM DeliveryProvider
            WHERE name = %s AND phone = %s;
        """
        values = (name, phone)
        return self._connection.get_many(query, values)

    def get_by_email_and_description(self, email: str, description: str) -> List[DeliveryProviderData]:
        query = """
            SELECT * FROM DeliveryProvider
            WHERE email = %s AND description = %s;
        """
        values = (email, description)
        return self._connection.get_many(query, values)
