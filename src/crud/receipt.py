from connections import PostgresDatabaseConection as DatabaseConnection
from DAO import ReceiptData
from typing import List

class ReceiptCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, receipt: ReceiptData) -> int:
        query = """
            INSERT INTO Receipt (id_shopping_cart_fk, id_payment_method_fk, id_transaction_status_fk, date_created, total)
            VALUES (%s, %s, %s, %s, %s);
        """
        values = (receipt.id_shopping_cart_fk, receipt.id_payment_method_fk, receipt.id_transaction_status_fk, receipt.date_created, receipt.total)
        return self._connection.create(query, values)
    
    def update(self, receipt: ReceiptData):
        query = """
            UPDATE Receipt
            SET id_shopping_cart_fk = %s, id_payment_method_fk = %s, id_transaction_status_fk = %s, date_created = %s, total = %s
            WHERE id_receipt = %s;
        """
        values = (receipt.id_shopping_cart_fk, receipt.id_payment_method_fk, receipt.id_transaction_status_fk, receipt.date_created, receipt.total, receipt.id_receipt)
        self._connection.update(query, values)
        
    def delete(self, receipt_id: int):
        query = """
            DELETE FROM Receipt
            WHERE id_receipt = %s;
        """
        self._connection.delete(query, receipt_id)
    
    def get_by_id(self, receipt_id: int) -> ReceiptData:
        query = """
            SELECT * FROM Receipt
            WHERE id_receipt = %s;
        """
        values = (receipt_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[ReceiptData]:
        query = """
            SELECT * FROM Receipt;
        """
        return self._connection.get_many(query)

    def get_receipt_with_cart(self, receipt_id: int) -> ReceiptData:
        query = """
            SELECT Receipt.*, ShoppingCart.total AS cart_total, ShoppingCart.date_created AS cart_date_created
            FROM Receipt
            JOIN ShoppingCart ON Receipt.id_shopping_cart_fk = ShoppingCart.id_shopping_cart
            WHERE Receipt.id_receipt = %s;
        """
        values = (receipt_id,)
        return self._connection.get_one(query, values)

    def get_receipt_with_payment_method(self, receipt_id: int) -> ReceiptData:
        query = """
            SELECT Receipt.*, PaymentMethods.type AS payment_type, PaymentMethods.provider AS payment_provider
            FROM Receipt
            JOIN PaymentMethods ON Receipt.id_payment_method_fk = PaymentMethods.id_payment_method
            WHERE Receipt.id_receipt = %s;
        """
        values = (receipt_id,)
        return self._connection.get_one(query, values)

    def get_receipt_with_transaction_status(self, receipt_id: int) -> ReceiptData:
        query = """
            SELECT Receipt.*, TransactionStatus.name AS status_name, TransactionStatus.description AS status_description
            FROM Receipt
            JOIN TransactionStatus ON Receipt.id_transaction_status_fk = TransactionStatus.id_transaction_status
            WHERE Receipt.id_receipt = %s;
        """
        values = (receipt_id,)
        return self._connection.get_one(query, values)

    def get_by_cart_and_payment_method(self, cart_id: int, payment_method_id: int) -> List[ReceiptData]:
        query = """
            SELECT * FROM Receipt
            WHERE id_shopping_cart_fk = %s AND id_payment_method_fk = %s;
        """
        values = (cart_id, payment_method_id)
        return self._connection.get_many(query, values)

    def get_by_transaction_status_and_total(self, status_id: int, total: float) -> List[ReceiptData]:
        query = """
            SELECT * FROM Receipt
            WHERE id_transaction_status_fk = %s AND total = %s;
        """
        values = (status_id, total)
        return self._connection.get_many(query, values)
    
    def get_by_date_created(self, date_created: str) -> List[ReceiptData]:
        query = """
            SELECT * FROM Receipt
            WHERE date_created = %s;
        """
        values = (date_created,)
        return self._connection.get_many(query, values)
    
    def get_by_total(self, total: float) -> List[ReceiptData]:
        query = """
            SELECT * FROM Receipt
            WHERE total = %s;
        """
        values = (total,)
        return self._connection.get_many(query, values)
    
    def get_by_cart_and_status(self, cart_id: int, status_id: int) -> List[ReceiptData]:
        query = """
            SELECT * FROM Receipt
            WHERE id_shopping_cart_fk = %s AND id_transaction_status_fk = %s;
        """
        values = (cart_id, status_id)
        return self._connection.get_many(query, values)
    
    def get_by_payment_method_and_status(self, payment_method_id: int, status_id: int) -> List[ReceiptData]:
        query = """
            SELECT * FROM Receipt
            WHERE id_payment_method_fk = %s AND id_transaction_status_fk = %s;
        """
        values = (payment_method_id, status_id)
        return self._connection.get_many(query, values)
