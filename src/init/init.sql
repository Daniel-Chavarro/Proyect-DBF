CREATE DATABASE IF NOT EXISTS MercadoLibre-XS;

CREATE TABLE Address (
    id_address INT PRIMARY KEY AUTO_INCREMENT,
    street VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    zip_code VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Brands (
    id_brand INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS TypeUsers (
    id_type_user INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS CategoryProduct (
    id_category INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE AccountStatus (
    id_account_status INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE StatusReport (
    id_status_report INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE ProductStatus (
    id_product_status INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE DeliveryProvider (
    id_delivery_provider INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100),
    description TEXT
);

CREATE TABLE DeliveryStatus (
    id_delivery_status INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE StatusCart (
    id_status_cart INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE TransactionStatus (
    id_transaction_status INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE CategoryReport (
    id_category_report INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE Store (
    id_store INT PRIMARY KEY AUTO_INCREMENT,
    id_user_fk INT NOT NULL,
    id_address_fk INT NOT NULL,
    name VARCHAR(100),
    description VARCHAR(255),
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_user_fk) REFERENCES Users(id_user),
    FOREIGN KEY (id_address_fk) REFERENCES Address(id_address)
);


CREATE TABLE PaymentMethods (
    id_payment_method INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(50) NOT NULL,
    provider VARCHAR(50),
    token VARCHAR(255) NOT NULL,
    owner VARCHAR(100)
);


CREATE TABLE Users (
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    id_address_fk INT NOT NULL,
    id_account_status_fk INT NOT NULL,
    id_type_user_fk INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    date_birth DATE NOT NULL,
    date_register TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    password VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_account_status_fk) REFERENCES AccountStatus(id_account_status),
    FOREIGN KEY (id_address_fk) REFERENCES Address(id_address)
    FOREIGN KEY (id_type_user_fk) REFERENCES TypeUsers(id_type_user)
);

CREATE TABLE Product (
    id_product INT PRIMARY KEY AUTO_INCREMENT,
    id_store_fk INT NOT NULL,
    id_product_status_fk INT NOT NULL,
    id_category_fk INT NOT NULL,
    id_brand_fk INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    date_published TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    rating DECIMAL(2,1) NOT NULL CHECK (rating BETWEEN 0.0 AND 5.0),
    FOREIGN KEY (id_brand_fk) REFERENCES Brands(id_brand),
    FOREIGN KEY (id_store_fk) REFERENCES Store(id_store),
    FOREIGN KEY (id_product_status_fk) REFERENCES ProductStatus(id_product_status),
    FOREIGN KEY (id_category_fk) REFERENCES CategoryProduct(id_category)
);

CREATE TABLE Delivery (
    id_delivery INT PRIMARY KEY AUTO_INCREMENT,
    id_user_fk INT NOT NULL,
    id_shopping_cart_fk INT NOT NULL,
    id_delivery_provider_fk INT NOT NULL,
    id_delivery_status_fk INT NOT NULL,
    id_address_fk INT NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_estimated_arrive DATE NOT NULL,
    delivery_cost DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_user_fk) REFERENCES Users(id_user),
    FOREIGN KEY (id_shopping_cart_fk) REFERENCES ShoppingCart(id_shopping_cart),
    FOREIGN KEY (id_delivery_status_fk) REFERENCES DeliveryStatus(id_delivery_status),
    FOREIGN KEY (id_delivery_provider_fk) REFERENCES DeliveryProvider(id_delivery_provider),
    FOREIGN KEY (id_address_fk) REFERENCES Address(id_address)
);

CREATE TABLE ShoppingCart (
    id_shopping_cart INT PRIMARY KEY AUTO_INCREMENT,
    id_status_cart_fk INT NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2) NOT NULL DEFAULT 0.0,
    FOREIGN KEY (id_user_fk) REFERENCES Users(id_user),
    FOREIGN KEY (id_status_cart_fk) REFERENCES StatusCart(id_status_cart)
);

CREATE TABLE CartItems (
    id_cart_item INT PRIMARY KEY AUTO_INCREMENT,
    id_shopping_cart_fk INT NOT NULL,
    id_product_fk INT NOT NULL,
    quantity INT NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_shopping_cart_fk) REFERENCES ShoppingCart(id_shopping_cart),
    FOREIGN KEY (id_product_fk) REFERENCES Product(id_product)
);

CREATE TABLE Receipt (
    id_receipt INT PRIMARY KEY AUTO_INCREMENT,
    id_shopping_cart_fk INT NOT NULL,
    id_payment_method_fk INT NOT NULL,
    id_transaction_status_fk INT NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_shopping_cart_fk) REFERENCES ShoppingCart(id_shopping_cart),
    FOREIGN KEY (id_payment_method_fk) REFERENCES PaymentMethods(id_payment_method),
    FOREIGN KEY (id_transaction_status_fk) REFERENCES TransactionStatus(id_transaction_status)
);

CREATE TABLE FavoritesListUsersStore (
    id_favorite_store INT PRIMARY KEY AUTO_INCREMENT,
    id_user_fk INT NOT NULL,
    id_store_fk INT NOT NULL,
    date_added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_user_fk) REFERENCES Users(id_user),
    FOREIGN KEY (id_store_fk) REFERENCES Store(id_store)
);

CREATE TABLE FavoriteListUsersProduct (
    id_favorite_product INT PRIMARY KEY AUTO_INCREMENT,
    id_user_fk INT NOT NULL,
    id_product_fk INT NOT NULL,
    date_added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_user_fk) REFERENCES Users(id_user),
    FOREIGN KEY (id_product_fk) REFERENCES Product(id_product)
);

CREATE TABLE ClientReport (
    id_client_report INT PRIMARY KEY AUTO_INCREMENT,
    id_user_reporter_fk INT NOT NULL,
    id_user_reported_fk INT NOT NULL,
    id_category_report_fk INT NOT NULL,
    id_status_report_fk INT NOT NULL,
    description TEXT,
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_user_reporter_fk) REFERENCES Users(id_user),
    FOREIGN KEY (id_user_reported_fk) REFERENCES Users(id_user),
    FOREIGN KEY (id_category_report_fk) REFERENCES CategoryReport(id_category_report),
    FOREIGN KEY (id_status_report_fk) REFERENCES StatusReport(id_status_report)
);
