CREATE DATABASE IF NOT EXISTS MercadoLibre-XS;

CREATE TABLE Address (
    ID_Address INT PRIMARY KEY AUTO_INCREMENT,
    Street VARCHAR(100),
    City VARCHAR(50),
    State VARCHAR(50),
    Country VARCHAR(50),
    ZipCode VARCHAR(20)
);

/*CREATE TABLE Ratings (
    ID_Rating INT PRIMARY KEY AUTO_INCREMENT,
    Entity_Type ENUM('Product', 'Seller') NOT NULL,
    ID_Entity INT NOT NULL,
    Rating DECIMAL(2, 1) CHECK (Rating BETWEEN 0.0 AND 5.0),
    ID_User_FK INT NOT NULL,
    Review_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Comments TEXT,
    FOREIGN KEY (ID_User_FK) REFERENCES User(ID_User)
);
*/

CREATE TABLE IF NOT EXISTS StatusReport (
    ID_Status_Report INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Description TEXT
);


CREATE TABLE IF NOT EXISTS ProductStatus (
    ID_Product_Status INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Description TEXT
);


CREATE TABLE IF NOT EXISTS DeliveryProvider (
    ID_Provider_Delivery INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Description TEXT
);


CREATE TABLE IF NOT EXISTS DeliveryStatus (
    ID_Status_Delivery INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Description TEXT
);


CREATE TABLE IF NOT EXISTS StatusCart (
    ID_Status_Cart INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Description TEXT
);


CREATE TABLE IF NOT EXISTS TransactionStatus (
    ID_Transaction_Status INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Description TEXT
);

CREATE TABLE IF NOT EXISTS CategoryReport (
    ID_Category_Report INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Description TEXT
);

CREATE TABLE IF NOT EXISTS Store(
	ID_Store INT PRIMARY KEY AUTO_INCREMENT,
	ID_Seller INT NOT NULL,
	Name VARCHAR(100),
	Date_Created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	Rating DECIMAL(2,1) CHECK (Rating BETWEEN 0.0 AND 5.0),
    FOREIGN KEY (ID_Seller) REFERENCES Seller(ID_Seller)
);

-- Tabla de métodos de pago
CREATE TABLE IF NOT EXISTS PaymentMethods (
    ID_Payment_Method INT PRIMARY KEY AUTO_INCREMENT,
    Type VARCHAR(50) NOT NULL,
    Provider VARCHAR(50),
    Card_Number VARCHAR(16),
    Date_Due DATE,
    Owner VARCHAR(100)
);


-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS User (
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
    ID_Account_Status_User INT NOT NULL,
    FOREIGN KEY (ID_Account_Status_User) REFERENCES AccountStatus(ID_Account_Status)
    FOREIGN KEY (ID_Address_FK) REFERENCES Address(ID_Address)
);

-- Tabla de vendedores
CREATE TABLE IF NOT EXISTS Seller (
    ID_Seller INT PRIMARY KEY AUTO_INCREMENT,
    First_Name VARCHAR(100) NOT NULL,
    Last_Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Phone VARCHAR(20) NOT NULL,
    Date_Register TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Password VARCHAR(100) NOT NULL,
    Date_Birth DATE NOT NULL,
    ID_Account_Status INT NOT NULL,
    Rating DECIMAL(2, 1) NOT NULL CHECK (Rating BETWEEN 0.0 AND 5.0),
    ID_Address_FK INT NOT NULL,
    FOREIGN KEY (ID_Account_Status) REFERENCES AccountStatus(ID_Account_Status)
    FOREIGN KEY (ID_Address_FK) REFERENCES Address(ID_Address)
);


-- Tabla de productos
CREATE TABLE IF NOT EXISTS Product (
    ID_Product INT PRIMARY KEY AUTO_INCREMENT,
    ID_Seller INT NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Description TEXT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Quantity_Stock INT NOT NULL,
    Category VARCHAR(50) NOT NULL,
    ID_Product_Status INT NOT NULL,
    Date_Published TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Brand VARCHAR(50) NOT NULL,
    Rating DECIMAL(2, 1) NOT NULL CHECK (Rating BETWEEN 0.0 AND 5.0),
    FOREIGN KEY (ID_Seller) REFERENCES Seller(ID_Seller),
    FOREIGN KEY (ID_Product_Status) REFERENCES ProductStatus(ID_Product_Status)
);



-- Tabla de entregas
CREATE TABLE IF NOT EXISTS Delivery (
    ID_Delivery INT PRIMARY KEY AUTO_INCREMENT,
    ID_User INT NOT NULL,
    ID_Product INT NOT NULL,
    Date_Created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Date_Estimated_Arrive DATE NOT NULL,
    ID_Status_Delivery INT NOT NULL,
    ID_Provider_Delivery INT NOT NULL,
    Delivery_Cost DECIMAL(10, 2) NOT NULL,
    ID_Address_FK INT  NOT NULL,
    FOREIGN KEY (ID_User) REFERENCES User(ID_User),
    FOREIGN KEY (ID_Product) REFERENCES Product(ID_Product),
    FOREIGN KEY (ID_Status_Delivery) REFERENCES DeliveryStatus(ID_Status_Delivery),
    FOREIGN KEY (ID_Provider_Delivery) REFERENCES DeliveryProvider(ID_Provider_Delivery)
    FOREIGN KEY (ID_Address_FK) REFERENCES Address(ID_Address)
);

-- Tabla de carrito de compras
CREATE TABLE IF NOT EXISTS ShoppingCart (
    ID_Shopping_Cart INT PRIMARY KEY AUTO_INCREMENT,
    ID_Status_Cart INT NOT NULL,
    ID_User INT NOT NULL,
    Date_Created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_User) REFERENCES User(ID_User)
    FOREIGN KEY (ID_Status_Cart) REFERENCES StatusCart(ID_Status_Cart)
);




CREATE TABLE CartItems (
    ID_Cart INT NOT NULL,
    ID_Product INT NOT NULL,
    Quantity INT NOT NULL,
    PRIMARY KEY (ID_Cart, ID_Product),
    FOREIGN KEY (ID_Cart) REFERENCES ShoppingCart(ID_Shopping_Cart),
    FOREIGN KEY (ID_Product) REFERENCES Product(ID_Product)
);



-- Tabla de transacciones
CREATE TABLE IF NOT EXISTS Transaction (
    ID_Transaction INT PRIMARY KEY AUTO_INCREMENT,
    ID_User INT NOT NULL,
    ID_Product INT NOT NULL,
    ID_Payment_Method INT NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    Date_Bought TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ID_Transaction_Status INT NOT NULL,
    FOREIGN KEY (ID_User) REFERENCES User(ID_User),
    FOREIGN KEY (ID_Product) REFERENCES Product(ID_Product),
    FOREIGN KEY (ID_Payment_Method) REFERENCES PaymentMethods(ID_Payment_Method),
    FOREIGN KEY (ID_Transaction_Status) REFERENCES TransactionStatus(ID_Transaction_Status)
);

CREATE TABLE IF NOT EXISTS Receipts (
    ID_Receipts INT PRIMARY KEY AUTO_INCREMENT,
    ID_Transaction INT NOT NULL,
    ID_User INT NOT NULL,
    Date_Created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Details TEXT,
    Amount_Paid DECIMAL(10, 2),
    Taxes DECIMAL(10, 2),
    FOREIGN KEY (ID_Transaction) REFERENCES Transaction(ID_Transaction),
    FOREIGN KEY (ID_User) REFERENCES User(ID_User)
);


CREATE TABLE IF NOT EXISTS FavoritesList (
    ID_Favorites_List INT PRIMARY KEY AUTO_INCREMENT,
    ID_User INT NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Date_Created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_User) REFERENCES User(ID_User)
);

CREATE TABLE FavoritesListSeller (
    ID_Favorites_List INT,
    ID_Seller INT,
    Date_Favorited TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (ID_Favorites_List, ID_Seller),
    FOREIGN KEY (ID_Favorites_List) REFERENCES FavoritesList(ID_Favorites_List),
    FOREIGN KEY (ID_Seller) REFERENCES Seller(ID_Seller)
);



CREATE TABLE IF NOT EXISTS ClientReport (
    ID_Report INT PRIMARY KEY AUTO_INCREMENT,
    ID_User INT NOT NULL,
    ID_Delivery INT,
    ID_Category_Report INT NOT NULL,
    Description TEXT,
    Date_Report TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ID_Status_Report INT NOT NULL,
    FOREIGN KEY (ID_User) REFERENCES User(ID_User),
    FOREIGN KEY (ID_Delivery) REFERENCES Delivery(ID_Delivery),
    FOREIGN KEY (ID_Category_Report) REFERENCES CategoryReport(ID_Category_Report),
    FOREIGN KEY (ID_Status_Report) REFERENCES StatusReport(ID_Status_Report)
);

	
CREATE TABLE IF NOT EXISTS UserDeliveryProvider (
    ID_User INT NOT NULL,
    ID_Provider_Delivery INT NOT NULL,
    Date_Assigned TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (ID_User, ID_Provider_Delivery),
    FOREIGN KEY (ID_User) REFERENCES User(ID_User),
    FOREIGN KEY (ID_Provider_Delivery) REFERENCES DeliveryProvider(ID_Provider_Delivery)
);

CREATE TABLE IF NOT EXISTS UserSeller (
    ID_User INT NOT NULL,
    ID_Seller INT NOT NULL,
    Date_Assigned TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (ID_User, ID_Seller),
    FOREIGN KEY (ID_User) REFERENCES User(ID_User),
    FOREIGN KEY (ID_Seller) REFERENCES Seller(ID_Seller)
);


CREATE TABLE IF NOT EXISTS DeliveryProduct (
    ID_Delivery INT NOT NULL,
    ID_Product INT NOT NULL,
    Quantity INT NOT NULL,
    PRIMARY KEY (ID_Delivery, ID_Product),
    FOREIGN KEY (ID_Delivery) REFERENCES Delivery(ID_Delivery),
    FOREIGN KEY (ID_Product) REFERENCES Product(ID_Product)
);