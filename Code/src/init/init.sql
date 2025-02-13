CREATE DATABASE IF NOT EXISTS MercadoLibre-XS;

CREATE TABLE Address (
    ID_Address INT PRIMARY KEY AUTO_INCREMENT,
    Street VARCHAR(100),
    City VARCHAR(50),
    State VARCHAR(50),
    Country VARCHAR(50),
    ZipCode VARCHAR(20)
);

CREATE TABLE AccountStatus (
    ID_Account_Status INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Description TEXT
);

CREATE TABLE StatusReport (
    ID_Status_Report INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Description TEXT
);

CREATE TABLE ProductStatus (
    ID_Product_Status INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Description TEXT
);

CREATE TABLE DeliveryProvider (
    ID_Provider_Delivery INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Description TEXT
);

CREATE TABLE DeliveryStatus (
    ID_Status_Delivery INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Description TEXT
);

CREATE TABLE StatusCart (
    ID_Status_Cart INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Description TEXT
);

CREATE TABLE TransactionStatus (
    ID_Transaction_Status INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Description TEXT
);

CREATE TABLE CategoryReport (
    ID_Category_Report INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Description TEXT
);

CREATE TABLE Store (
    ID_Store INT PRIMARY KEY AUTO_INCREMENT,
    ID_User_FK INT NOT NULL,
    Name VARCHAR(100),
    Date_Created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Rating DECIMAL(2,1) CHECK (Rating BETWEEN 0.0 AND 5.0),
    FOREIGN KEY (ID_User_FK) REFERENCES User(ID_User)
);

CREATE TABLE PaymentMethods (
    ID_Payment_Method INT PRIMARY KEY AUTO_INCREMENT,
    Type VARCHAR(50) NOT NULL,
    Provider VARCHAR(50),
    Token VARCHAR(255) NOT NULL,
    Owner VARCHAR(100)
);

CREATE TABLE User (
    ID_User INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Last_Name VARCHAR(100) NOT NULL,
    Username VARCHAR(50) NOT NULL UNIQUE,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Phone VARCHAR(20) NOT NULL,
    Date_Registered TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Password VARCHAR(100) NOT NULL,
    Date_Birth DATE NOT NULL,
    ID_Address_FK INT NOT NULL,
    ID_Account_Status_FK INT NOT NULL,
    FOREIGN KEY (ID_Account_Status_FK) REFERENCES AccountStatus(ID_Account_Status),
    FOREIGN KEY (ID_Address_FK) REFERENCES Address(ID_Address)
);

CREATE TABLE Product (
    ID_Product INT PRIMARY KEY AUTO_INCREMENT,
    ID_User_FK INT NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Description TEXT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Quantity_Stock INT NOT NULL,
    Category VARCHAR(50) NOT NULL,
    ID_Product_Status_FK INT NOT NULL,
    Date_Published TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Brand VARCHAR(50) NOT NULL,
    Rating DECIMAL(2,1) NOT NULL CHECK (Rating BETWEEN 0.0 AND 5.0),
    FOREIGN KEY (ID_User_FK) REFERENCES User(ID_User),
    FOREIGN KEY (ID_Product_Status_FK) REFERENCES ProductStatus(ID_Product_Status)
);

CREATE TABLE Delivery (
    ID_Delivery INT PRIMARY KEY AUTO_INCREMENT,
    ID_User_FK INT NOT NULL,
    ID_Product_FK INT NOT NULL,
    Date_Created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Date_Estimated_Arrive DATE NOT NULL,
    ID_Status_Delivery_FK INT NOT NULL,
    ID_Provider_Delivery_FK INT NOT NULL,
    Delivery_Cost DECIMAL(10, 2) NOT NULL,
    ID_Address_FK INT NOT NULL,
    FOREIGN KEY (ID_User_FK) REFERENCES User(ID_User),
    FOREIGN KEY (ID_Product_FK) REFERENCES Product(ID_Product),
    FOREIGN KEY (ID_Status_Delivery_FK) REFERENCES DeliveryStatus(ID_Status_Delivery),
    FOREIGN KEY (ID_Provider_Delivery_FK) REFERENCES DeliveryProvider(ID_Provider_Delivery),
    FOREIGN KEY (ID_Address_FK) REFERENCES Address(ID_Address)
);

CREATE TABLE ShoppingCart (
    ID_Shopping_Cart INT PRIMARY KEY AUTO_INCREMENT,
    ID_Status_Cart_FK INT NOT NULL,
    ID_User_FK INT NOT NULL,
    Date_Created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_User_FK) REFERENCES User(ID_User),
    FOREIGN KEY (ID_Status_Cart_FK) REFERENCES StatusCart(ID_Status_Cart)
);

CREATE TABLE CartItems (
    ID_Cart_FK INT NOT NULL,
    ID_Product_FK INT NOT NULL,
    Quantity INT NOT NULL,
    PRIMARY KEY (ID_Cart_FK, ID_Product_FK),
    FOREIGN KEY (ID_Cart_FK) REFERENCES ShoppingCart(ID_Shopping_Cart),
    FOREIGN KEY (ID_Product_FK) REFERENCES Product(ID_Product)
);

CREATE TABLE Receipt (
    ID_Transaction INT PRIMARY KEY AUTO_INCREMENT,
    ID_User_FK INT NOT NULL,
    ID_Product_FK INT NOT NULL,
    ID_Payment_Method_FK INT NOT NULL,
    Taxes DECIMAL(10, 2) NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    Date_Bought TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Description VARCHAR(100),
    ID_Transaction_Status_FK INT NOT NULL,
    FOREIGN KEY (ID_User_FK) REFERENCES User(ID_User),
    FOREIGN KEY (ID_Product_FK) REFERENCES Product(ID_Product),
    FOREIGN KEY (ID_Payment_Method_FK) REFERENCES PaymentMethods(ID_Payment_Method),
    FOREIGN KEY (ID_Transaction_Status_FK) REFERENCES TransactionStatus(ID_Transaction_Status)
);

CREATE TABLE FavoritesListUserStore (
    ID_Favorites_List INT PRIMARY KEY AUTO_INCREMENT,
    ID_User_FK INT NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Date_Created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_User_FK) REFERENCES User(ID_User)
);

CREATE TABLE FavoriteListUserProduct (
    ID_Favorites_List INT PRIMARY KEY AUTO_INCREMENT,
    ID_User_FK INT NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Date_Created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_User_FK) REFERENCES User(ID_User)
);

CREATE TABLE FavoritesListUser (
    ID_Favorites_List_FK INT NOT NULL,
    ID_User_FK INT NOT NULL,
    Date_Favorited TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (ID_Favorites_List_FK, ID_User_FK),
    FOREIGN KEY (ID_Favorites_List_FK) REFERENCES FavoriteListUserProduct(ID_Favorites_List),
    FOREIGN KEY (ID_User_FK) REFERENCES User(ID_User)
);

CREATE TABLE ClientReport (
    ID_Report INT PRIMARY KEY AUTO_INCREMENT,
    ID_User_FK INT NOT NULL,
    ID_Delivery_FK INT,
    ID_Category_Report_FK INT NOT NULL,
    Description TEXT,
    Date_Report TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ID_Status_Report_FK INT NOT NULL,
    FOREIGN KEY (ID_User_FK) REFERENCES User(ID_User),
    FOREIGN KEY (ID_Delivery_FK) REFERENCES Delivery(ID_Delivery),
    FOREIGN KEY (ID_Category_Report_FK) REFERENCES CategoryReport(ID_Category_Report),
    FOREIGN KEY (ID_Status_Report_FK) REFERENCES StatusReport(ID_Status_Report)
);

CREATE TABLE UserDeliveryProvider (
    ID_User_FK INT NOT NULL,
    ID_Provider_Delivery_FK INT NOT NULL,
    Date_Assigned TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (ID_User_FK, ID_Provider_Delivery_FK),
    FOREIGN KEY (ID_User_FK) REFERENCES User(ID_User),
    FOREIGN KEY (ID_Provider_Delivery_FK) REFERENCES DeliveryProvider(ID_Provider_Delivery)
);
