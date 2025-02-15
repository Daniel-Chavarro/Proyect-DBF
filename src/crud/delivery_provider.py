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
    
    def get_by_name(self, name: str) -> DeliveryProviderData:
        query = """
            SELECT * FROM DeliveryProvider
            WHERE LOWER(name) LIKE LOWER(%s);
        """
        values = (f"%{name}%",)
        return self._connection.get_many(query, values)
    
    def get_by_phone(self, phone: str) -> DeliveryProviderData:
        query = """
            SELECT * FROM DeliveryProvider
            WHERE phone = %s;
        """
        values = (phone,)
        return self._connection.get_many(query, values)
    
    def get_by_email(self, email: str) -> DeliveryProviderData:
        query = """
            SELECT * FROM DeliveryProvider
            WHERE email = %s;
        """
        values = (email,)
        return self._connection.get_many(query, values)
