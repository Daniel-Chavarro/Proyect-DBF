from connections import DatabaseConnection
from DAO import PaymentMethodData
from typing import List

class PaymentMethodCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, payment_method: PaymentMethodData) -> int:
        query = """
            INSERT INTO PaymentMethods (type, provider, token, owner)
            VALUES (%s, %s, %s, %s);
        """
        values = (payment_method.type, payment_method.provider, payment_method.token, payment_method.owner)
        return self._connection.create(query, values)
    
    def update(self, payment_method: PaymentMethodData):
        query = """
            UPDATE PaymentMethods
            SET type = %s, provider = %s, token = %s, owner = %s
            WHERE id_payment_method = %s;
        """
        values = (payment_method.type, payment_method.provider, payment_method.token, payment_method.owner, payment_method.id_payment_method)
        self._connection.update(query, values)
        
    def delete(self, payment_method_id: int):
        query = """
            DELETE FROM PaymentMethods
            WHERE id_payment_method = %s;
        """
        self._connection.delete(query, payment_method_id)
    
    def get_by_id(self, payment_method_id: int) -> PaymentMethodData:
        query = """
            SELECT * FROM PaymentMethods
            WHERE id_payment_method = %s;
        """
        values = (payment_method_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[PaymentMethodData]:
        query = """
            SELECT * FROM PaymentMethods;
        """
        return self._connection.get_many(query)

    def get_by_type(self, type: str) -> List[PaymentMethodData]:
        query = """
            SELECT * FROM PaymentMethods
            WHERE type = %s;
        """
        values = (type,)
        return self._connection.get_many(query, values)
    
    def get_by_provider(self, provider: str) -> List[PaymentMethodData]:
        query = """
            SELECT * FROM PaymentMethods
            WHERE provider = %s;
        """
        values = (provider,)
        return self._connection.get_many(query, values)
    
    def get_by_token(self, token: str) -> PaymentMethodData:
        query = """
            SELECT * FROM PaymentMethods
            WHERE token = %s;
        """
        values = (token,)
        return self._connection.get_one(query, values)