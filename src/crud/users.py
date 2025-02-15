from connections import DatabaseConnection
from DAO import UserData
from typing import List

class UsersCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, user: UserData) -> int:
        query = """
            INSERT INTO Users (id_user,id_address_fk, id_account_status_fk, id_type_user_fk, name, last_name, username, email, phone, date_birth, date_register, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        
        values = (user.id_user ,user.id_address_fk, user.id_account_status_fk, user.id_type_user_fk, user.name, user.last_name, user.username, user.email, user.phone, user.date_birth, user.date_register, user.password)
        return self._connection.create(query, values)
    
    def update(self, user: UserData):
        query = """
            UPDATE Users
            SET id_address_fk = %s, id_account_status_fk = %s, id_type_user_fk = %s, name = %s, last_name = %s, username = %s, email = %s, phone = %s, date_birth = %s, date_register = %s, password = %s
            WHERE id_user = %s;
        """
        
        values = (user.id_user,user.id_address_fk, user.id_account_status_fk, user.id_type_user_fk, user.name, user.last_name, user.username, user.email, user.phone, user.date_birth, user.date_register, user.password)
        self._connection.update(query, values)
        
    def delete(self, user_id: int):
        query = """
            DELETE FROM Users
            WHERE id_user = %s;
        """
        values = (user_id,)
        self._connection.delete(query, values)
    
    def get_by_id(self, user_id: int) -> UserData:
        query = """
            SELECT Users.* , AccountStatus.name AS status, TypeUsers.name AS role  
            FROM Users
            WHERE Users.id_user = %s
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = account_status.id_account_status;
        """
        values = (user_id,)
        
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[UserData]:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status;
        """
        
        return self._connection.get_many(query)
    
    def get_by_username(self, username: str) -> UserData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE LOWER(Users.username) LIKE LOWER(%s);
        """
        values = (f"{username}",)
        return self._connection.get_one(query, values)

    def get_by_email(self, email: str) -> UserData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE Users.email LIKE %s;
        """
        
        values = (email,)
        return self._connection.get_one(query, values)

    def get_by_phone(self, phone: str) -> UserData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE Users.phone LIKE %s;
        """
        values = (phone,)
        return self._connection.get_one(query, values)

    def get_by_name(self, name: str) -> UserData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE LOWER(Users.name) LIKE LOWER(%s);
        
        """
        
        values = (f"%{name}%",)
        return self._connection.get_one(query, values)
    
    def get_by_last_name(self, last_name: str) -> UserData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE LOWER(Users.last_name) LIKE LOWER(%s);
        """
        values = (f"%{last_name}%",)
        return self._connection.get_many(query, values)
    
    def get_by_role(self, role: str) -> List[UserData]:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE LOWER(TypeUser.name) LIKE LOWER(%s);
        """
        values = (f"%{role}%",)
        return self._connection.get_many(query, values)
    
    def get_by_id_status(self, id_status: int) -> List[UserData]:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE AccountStatus.id_account_status = %s;
        """
        values = (id_status,)
        return self._connection.get_many(query, values)

    def get_by_id_type_user(self, type_user: int) -> List[UserData]:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS role 
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            WHERE TypeUser.id_type_user = %s;
        """
        values = (type_user,)
        return self._connection.get_many(query, values)
    
    def get_user_with_address(self, id_user: int) -> UserData:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS role, Address.country as country, Address.city as city
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            JOIN Address ON Users.id_address_fk = Address.id_address
            WHERE Users.id_user = %s;
        """
        values = (id_user,)
        return self._connection.get_one(query, values)
    
    def get_all_users_with_address(self) -> List[UserData]:
        query = """
            SELECT Users.*, AccountStatus.name AS status, TypeUser.name AS role , Address.country as country, Address.city as city
            FROM Users
            JOIN TypeUsers ON Users.id_type_user_fk = TypeUser.id_type_user
            JOIN AccountStatus ON Users.id_account_status_fk = AccountStatus.id_account_status
            JOIN Address ON Users.id_address_fk = Address.id_address;
        """
        
        return self._connection.get_many(query)
    
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