from connections import PostgresDatabaseConection as DatabaseConnection
from DAO import UsersData
from typing import List

class UsersCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, user: UsersData) -> int:
        query = """
            INSERT INTO Users (id_address_fk, id_account_status_fk, id_type_user_fk, name, last_name, username, email, phone, date_birth, date_register, password, is_active, is_superuser)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        
        values = (user.id_address_fk, user.id_account_status_fk, user.id_type_user_fk, user.name, user.last_name, user.username, user.email, user.phone, user.date_birth, user.date_register, user.password, user.is_active, user.is_superuser)
        return self._connection.create(query, values)
    
    def update(self, user: UsersData):
        query = """
            UPDATE Users
            SET id_address_fk = %s, id_account_status_fk = %s, id_type_user_fk = %s, name = %s, last_name = %s, username = %s, email = %s, phone = %s, date_birth = %s, date_register = %s, password = %s, is_active = %s, is_superuser = %s
            WHERE id_user = %s;
        """
        
        values = (user.id_address_fk, user.id_account_status_fk, user.id_type_user_fk, user.name, user.last_name, user.username, user.email, user.phone, user.date_birth, user.date_register, user.password, user.is_active, user.is_superuser, user.id_user)
        self._connection.update(query, values)
        
    def delete(self, user_id: int):
        query = """
            DELETE FROM Users
            WHERE id_user = %s;
        """
        
        self._connection.delete(query, user_id)
    
    def get_by_id(self, user_id: int) -> UsersData:
        query = """
            SELECT Users.* , AccountStatus.name AS status, TypeUsers.name AS Role  
            FROM Users
            WHERE Users.id_user = %s
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = account_status.id_account_status;
        """
        values = (user_id,)
        
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[UsersData]:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status;
        """
        
        return self._connection.get_many(query)
    
    def get_by_username(self, username: str) -> UsersData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE LOWER(Users.username) LIKE LOWER(%s);
        """
        values = (f"%{username}%")
        return self._connection.get_one(query, values)

    def get_by_email(self, email: str) -> UsersData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE Users.email LIKE %s;
        """
        
        values = (email,)
        return self._connection.get_one(query, values)

    def get_by_phone(self, phone: str) -> UsersData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE Users.phone LIKE %s;
        """
        values = (phone,)
        return self._connection.get_one(query, values)

    def get_by_name(self, name: str) -> UsersData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE LOWER(Users.name) LIKE LOWER(%s);
        
        """
        
        values = (f"%{name}%")
        return self._connection.get_one(query, values)
    
    def get_by_last_name(self, last_name: str) -> UsersData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE LOWER(Users.last_name) LIKE LOWER(%s);
        """
        values = (f"%{last_name}%")
        return self._connection.get_one(query, values)
    
    def get_by_role(self, role: str) -> List[UsersData]:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE LOWER(TypeUser.name) LIKE LOWER(%s);
        """
        values = (f"%{role}%")
        return self._connection.get_many(query, values)
    
    def get_by_id_status(self, id_status: int) -> List[UsersData]:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE AccountStatus.id_account_status = %s;
        """
        values = (id_status,)
        return self._connection.get_many(query, id_status)

    def get_by_id_type_user(self, type_user: int) -> List[UsersData]:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE TypeUser.id_type_user = %s;
        """
        
        return self._connection.get_many(query, type_user)
    
    def get_user_with_address(self, id_user: int) -> UsersData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role, Address.*
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            JOIN Address ON Users.id_address_fk = Address.id_address
            WHERE Users.id_user = %s;
        """
        values = (id_user,)
        return self._connection.get_one(query, values)
    
    def get_all_users_with_address(self) -> List[UsersData]:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role, Address.*
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            JOIN Address ON Users.id_address_fk = Address.id_address;
        """
        
        return self._connection.get_many(query)
    
    def get_user_purchases(self, id_user: int) -> List[UsersData]:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role, Receipt.*
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            JOIN Receipt ON Users.id_user = Receipt.id_user_fk
            WHERE Users.id_user = %s;
        """
        
        values = (id_user,)
        return self._connection.get_many(query, values)

    def get_user_purchases_payment_method(self, id_user: int) -> UsersData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role, Receipt.*, PaymentMethods.*
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            JOIN Receipt ON Users.id_user = Receipt.id_user_fk
            JOIN PaymentMethods ON Receipt.id_payment_method_fk = PaymentMethods.id_payment_method
            WHERE Users.id_user = %s;
        """
        
        values = (id_user,)
        return self._connection.get_many(query, values)
    
    def get_full_purchases_info(self, id_user: int) -> UsersData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role, ShoppingCart.id_shopping_cart, PaymentMethods.id_payment_method, PaymentMethods.token , Receipt.*
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            JOIN Receipt ON Users.id_user = Receipt.id_user_fk
            JOIN PaymentMethods ON Receipt.id_payment_method_fk = PaymentMethods.id_payment_method
            JOIN ShoppingCart ON Receipt.id_shopping_cart_fk = ShoppingCart.id_shopping_cart
            WHERE Users.id_user = %s;
        """
        values = (id_user,)
        return self._connection.get_many(query, values)
    
    def get_user_purchase_by_id(self, id_user: int, id_receipt: str) -> UsersData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role, Receipt.*
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            JOIN Receipt ON Users.id_user = Receipt.id_user_fk
            WHERE Users.id_user = %s AND Receipt.id_receipt = %s;
        """
        values = (id_user, id_receipt)
        return self._connection.get_one(query, values)
    
    def get_user_purchase_full_by_id(self, id_user: int, id_receipt: str) -> UsersData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS Role, Receipt.*, PaymentMethods.*, Products.*
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            JOIN Receipt ON Users.id_user = Receipt.id_user_fk
            JOIN PaymentMethods ON Receipt.id_payment_method_fk = PaymentMethods.id_payment_method
            JOIN Products ON Receipt.id_product_fk = Products.id_product
            WHERE Users.id_user = %s AND Receipt.id_receipt = %s;
        """
        values = (id_user, id_receipt)
        return self._connection.get_one(query, values)

    def get_user_shopping_cart(self, id_user: int) -> UsersData:
        query = """
            SELECT Users.*, ShoppingCart.*, CartItems.*
            FROM Users
            JOIN ShoppingCart ON Users.id_user = ShoppingCart.id_user_fk
            JOIN CartItems ON ShoppingCart.id_shopping_cart = CartItems.id_shopping_cart_fk
            WHERE Users.id_user = %s;
        """
        values = (id_user,)
        return self._connection.get_many(query, values)

    def validate_seller(self, id_user: int) -> bool:
        query = """
            SELECT TypeUsers.name
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUsers.id_type_user
            WHERE Users.id_user = %s AND TypeUsers.id_type_user = 1;
        """
        values = (id_user,)
        result = self._connection.get_one(query, values)
        return result is not None