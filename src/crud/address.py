from connections import PostgresDatabaseConection as DatabaseConnection
from DAO import AddressData
from typing import List

class AddressCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, address: AddressData) -> int:
        query = """
            INSERT INTO Address (street, city, state, country, zip_code)
            VALUES (%s, %s, %s, %s, %s);
        """
        values = (address.street, address.city, address.state, address.country, address.zip_code)
        return self._connection.create(query, values)
    
    def update(self, address: AddressData):
        query = """
            UPDATE Address
            SET street = %s, city = %s, state = %s, country = %s, zip_code = %s
            WHERE id_address = %s;
        """
        values = (address.street, address.city, address.state, address.country, address.zip_code, address.id_address)
        self._connection.update(query, values)
        
    def delete(self, address_id: int):
        query = """
            DELETE FROM Address
            WHERE id_address = %s;
        """
        self._connection.delete(query, address_id)
    
    def get_by_id(self, address_id: int) -> AddressData:
        query = """
            SELECT * FROM Address
            WHERE id_address = %s;
        """
        values = (address_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[AddressData]:
        query = """
            SELECT * FROM Address;
        """
        return self._connection.get_many(query)

    def get_by_city(self, city: str) -> List[AddressData]:
        query = """
            SELECT * FROM Address
            WHERE city = %s;
        """
        values = (city,)
        return self._connection.get_many(query, values)

    def get_by_state(self, state: str) -> List[AddressData]:
        query = """
            SELECT * FROM Address
            WHERE state = %s;
        """
        values = (state,)
        return self._connection.get_many(query, values)

    def get_by_country(self, country: str) -> List[AddressData]:
        query = """
            SELECT * FROM Address
            WHERE country = %s;
        """
        values = (country,)
        return self._connection.get_many(query, values)

    def get_by_zip_code(self, zip_code: str) -> List[AddressData]:
        query = """
            SELECT * FROM Address
            WHERE zip_code = %s;
        """
        values = (zip_code,)
        return self._connection.get_many(query, values)

    def get_by_city_and_state(self, city: str, state: str) -> List[AddressData]:
        query = """
            SELECT * FROM Address
            WHERE city = %s AND state = %s;
        """
        values = (city, state)
        return self._connection.get_many(query, values)

    def get_by_zip_code_and_country(self, zip_code: str, country: str) -> List[AddressData]:
        query = """
            SELECT * FROM Address
            WHERE zip_code = %s AND country = %s;
        """
        values = (zip_code, country)
        return self._connection.get_many(query, values)

    def get_by_zip_code_and_state(self, zip_code: str, state: str) -> List[AddressData]:
        query = """
            SELECT * FROM Address
            WHERE zip_code = %s AND state = %s;
        """
        values = (zip_code, state)
        return self._connection.get_many(query, values)

    def get_by_state_and_street(self, state: str, street: str) -> List[AddressData]:
        query = """
            SELECT * FROM Address
            WHERE state = %s AND street = %s;
        """
        values = (state, street)
        return self._connection.get_many(query, values)

    def get_by_city_and_country(self, city: str, country: str) -> List[AddressData]:
        query = """
            SELECT * FROM Address
            WHERE city = %s AND country = %s;
        """
        values = (city, country)
        return self._connection.get_many(query, values)

    def get_by_state_and_zip_code(self, state: str, zip_code: str) -> List[AddressData]:
        query = """
            SELECT * FROM Address
            WHERE state = %s AND zip_code = %s;
        """
        values = (state, zip_code)
        return self._connection.get_many(query, values)

    def get_by_city_and_state_and_zip_code(self, city: str, state: str, zip_code: str) -> List[AddressData]:
        query = """
            SELECT * FROM Address
            WHERE city = %s AND state = %s AND zip_code = %s;
        """
        values = (city, state, zip_code)
        return self._connection.get_many(query, values)

    def get_by_country_and_state_and_street(self, country: str, state: str, street: str) -> List[AddressData]:
        query = """
            SELECT * FROM Address
            WHERE country = %s AND state = %s AND street = %s;
        """
        values = (country, state, street)
        return self._connection.get_many(query, values)

    def get_address_with_user(self, address_id: int) -> AddressData:
        query = """
            SELECT Address.*, Users.name AS user_name, Users.email AS user_email
            FROM Address
            JOIN Users ON Address.id_address = Users.id_address_fk
            WHERE Address.id_address = %s;
        """
        values = (address_id,)
        return self._connection.get_one(query, values)
