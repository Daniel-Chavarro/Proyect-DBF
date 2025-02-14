from connections import PostgresDatabaseConection as DatabaseConnection
from DAO import ProductData
from typing import List

class ProductCRUD():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
    
    def create(self, product: ProductData) -> int:
        query = """
            INSERT INTO Product (id_store_fk, id_product_status_fk, id_category_fk, id_brand_fk, name, description, price, stock, date_published, rating)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        values = (product.id_store_fk, product.id_product_status_fk, product.id_category_fk, product.id_brand_fk, product.name, product.description, product.price, product.stock, product.date_published, product.rating)
        return self._connection.create(query, values)
    
    def update(self, product: ProductData):
        query = """
            UPDATE Product
            SET id_store_fk = %s, id_product_status_fk = %s, id_category_fk = %s, id_brand_fk = %s, name = %s, description = %s, price = %s, stock = %s, date_published = %s, rating = %s
            WHERE id_product = %s;
        """
        values = (product.id_store_fk, product.id_product_status_fk, product.id_category_fk, product.id_brand_fk, product.name, product.description, product.price, product.stock, product.date_published, product.rating, product.id_product)
        self._connection.update(query, values)
        
    def delete(self, product_id: int):
        query = """
            DELETE FROM Product
            WHERE id_product = %s;
        """
        self._connection.delete(query, product_id)
    
    def get_by_id(self, product_id: int) -> ProductData:
        query = """
            SELECT * FROM Product
            WHERE id_product = %s;
        """
        values = (product_id,)
        return self._connection.get_one(query, values)
    
    def get_all(self) -> List[ProductData]:
        query = """
            SELECT * FROM Product;
        """
        return self._connection.get_many(query)
    
    def get_by_store_id(self, store_id: int) -> List[ProductData]:
        query = """
            SELECT * FROM Product
            WHERE id_store_fk = %s;
        """
        values = (store_id,)
        return self._connection.get_many(query, values)

    def get_by_category_id(self, category_id: int) -> List[ProductData]:
        query = """
            SELECT * FROM Product
            WHERE id_category_fk = %s;
        """
        values = (category_id,)
        return self._connection.get_many(query, values)

    def get_by_brand_id(self, brand_id: int) -> List[ProductData]:
        query = """
            SELECT * FROM Product
            WHERE id_brand_fk = %s;
        """
        values = (brand_id,)
        return self._connection.get_many(query, values)

    def get_by_status_id(self, status_id: int) -> List[ProductData]:
        query = """
            SELECT * FROM Product
            WHERE id_product_status_fk = %s;
        """
        values = (status_id,)
        return self._connection.get_many(query, values)

    def get_product_with_store(self, product_id: int) -> ProductData:
        query = """
            SELECT Product.*, Store.name AS store_name, Store.description AS store_description
            FROM Product
            JOIN Store ON Product.id_store_fk = Store.id_store
            WHERE Product.id_product = %s;
        """
        values = (product_id,)
        return self._connection.get_one(query, values)

    def get_product_with_category(self, product_id: int) -> ProductData:
        query = """
            SELECT Product.*, CategoryProduct.name AS category_name, CategoryProduct.description AS category_description
            FROM Product
            JOIN CategoryProduct ON Product.id_category_fk = CategoryProduct.id_category
            WHERE Product.id_product = %s;
        """
        values = (product_id,)
        return self._connection.get_one(query, values)

    def get_product_with_brand(self, product_id: int) -> ProductData:
        query = """
            SELECT Product.*, Brands.name AS brand_name, Brands.description AS brand_description
            FROM Product
            JOIN Brands ON Product.id_brand_fk = Brands.id_brand
            WHERE Product.id_product = %s;
        """
        values = (product_id,)
        return self._connection.get_one(query, values)

    def get_product_with_status(self, product_id: int) -> ProductData:
        query = """
            SELECT Product.*, ProductStatus.name AS status_name, ProductStatus.description AS status_description
            FROM Product
            JOIN ProductStatus ON Product.id_product_status_fk = ProductStatus.id_product_status
            WHERE Product.id_product = %s;
        """
        values = (product_id,)
        return self._connection.get_one(query, values)

    def get_by_store_and_category(self, store_id: int, category_id: int) -> List[ProductData]:
        query = """
            SELECT * FROM Product
            WHERE id_store_fk = %s AND id_category_fk = %s;
        """
        values = (store_id, category_id)
        return self._connection.get_many(query, values)

    def get_by_brand_and_status(self, brand_id: int, status_id: int) -> List[ProductData]:
        query = """
            SELECT * FROM Product
            WHERE id_brand_fk = %s AND id_product_status_fk = %s;
        """
        values = (brand_id, status_id)
        return self._connection.get_many(query, values)

    def get_by_store_and_status(self, store_id: int, status_id: int) -> List[ProductData]:
        query = """
            SELECT * FROM Product
            WHERE id_store_fk = %s AND id_product_status_fk = %s;
        """
        values = (store_id, status_id)
        return self._connection.get_many(query, values)

    def get_by_category_and_brand(self, category_id: int, brand_id: int) -> List[ProductData]:
        query = """
            SELECT * FROM Product
            WHERE id_category_fk = %s AND id_brand_fk = %s;
        """
        values = (category_id, brand_id)
        return self._connection.get_many(query, values)
