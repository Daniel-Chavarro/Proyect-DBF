# Project DBF

## Overview

Project DBF is a backend application designed to manage various entities similar to a smaller version of Mercado Libre. The application provides CRUD (Create, Read, Update, Delete) operations for multiple entities such as users, products, orders, payments, categories, reviews, addresses, and more.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Entities](#entities)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/Proyect-DBF.git
    cd Proyect-DBF
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database connection in `connections/database_connection.py`.

## Usage

1. Run the FastAPI application:
    ```sh
    uvicorn main:app --reload
    ```


## API Endpoints

### User

- `POST /user/create`: Create a new user.
- `PUT /user/update/{id_}`: Update an existing user.
- `DELETE /user/delete/{id_}`: Delete a user.
- `GET /user/get_by_id/{id_}`: Get a user by ID.
- `GET /user/get_all`: Get all users.

### Product

- `POST /product/create`: Create a new product.
- `PUT /product/update/{id_}`: Update an existing product.
- `DELETE /product/delete/{id_}`: Delete a product.
- `GET /product/get_by_id/{id_}`: Get a product by ID.
- `GET /product/get_all`: Get all products.

### Cart

- `POST /cart/create`: Create a new cart.
- `PUT /cart/update/{id_}`: Update an existing cart.
- `DELETE /cart/delete/{id_}`: Delete a cart.
- `GET /cart/get_by_id/{id_}`: Get a cart by ID.
- `GET /cart/get_all`: Get all carts.

### Order

- `POST /order/create`: Create a new order.
- `PUT /order/update/{id_}`: Update an existing order.
- `DELETE /order/delete/{id_}`: Delete an order.
- `GET /order/get_by_id/{id_}`: Get an order by ID.
- `GET /order/get_all`: Get all orders.

### Payment

- `POST /payment/create`: Create a new payment.
- `PUT /payment/update/{id_}`: Update an existing payment.
- `DELETE /payment/delete/{id_}`: Delete a payment.
- `GET /payment/get_by_id/{id_}`: Get a payment by ID.
- `GET /payment/get_all`: Get all payments.

### Category

- `POST /category/create`: Create a new category.
- `PUT /category/update/{id_}`: Update an existing category.
- `DELETE /category/delete/{id_}`: Delete a category.
- `GET /category/get_by_id/{id_}`: Get a category by ID.
- `GET /category/get_all`: Get all categories.

### Review

- `POST /review/create`: Create a new review.
- `PUT /review/update/{id_}`: Update an existing review.
- `DELETE /review/delete/{id_}`: Delete a review.
- `GET /review/get_by_id/{id_}`: Get a review by ID.
- `GET /review/get_all`: Get all reviews.

### Address

- `POST /address/create`: Create a new address.
- `PUT /address/update/{id_}`: Update an existing address.
- `DELETE /address/delete/{id_}`: Delete an address.
- `GET /address/get_by_id/{id_}`: Get an address by ID.
- `GET /address/get_all`: Get all addresses.

### Store

- `POST /store/create`: Create a new store.
- `PUT /store/update/{id_}`: Update an existing store.
- `DELETE /store/delete/{id_}`: Delete a store.
- `GET /store/get_by_id/{id_}`: Get a store by ID.
- `GET /store/get_all`: Get all stores.

### Transaction Status

- `POST /transaction_status/create`: Create a new transaction status.
- `PUT /transaction_status/update/{id_}`: Update an existing transaction status.
- `DELETE /transaction_status/delete/{id_}`: Delete a transaction status.
- `GET /transaction_status/get_by_id/{id_}`: Get a transaction status by ID.
- `GET /transaction_status/get_all`: Get all transaction statuses.

### Status Report

- `POST /status_report/create`: Create a new status report.
- `PUT /status_report/update/{id_}`: Update an existing status report.
- `DELETE /status_report/delete/{id_}`: Delete a status report.
- `GET /status_report/get_by_id/{id_}`: Get a status report by ID.
- `GET /status_report/get_all`: Get all status reports.

### Category Report

- `POST /category_report/create`: Create a new category report.
- `PUT /category_report/update/{id_}`: Update an existing category report.
- `DELETE /category_report/delete/{id_}`: Delete a category report.
- `GET /category_report/get_by_id/{id_}`: Get a category report by ID.
- `GET /category_report/get_all`: Get all category reports.

### Client Report

- `POST /client_report/create`: Create a new client report.
- `PUT /client_report/update/{id_}`: Update an existing client report.
- `DELETE /client_report/delete/{id_}`: Delete a client report.
- `GET /client_report/get_by_id/{id_}`: Get a client report by ID.
- `GET /client_report/get_all`: Get all client reports.

### Delivery

- `POST /delivery/create`: Create a new delivery.
- `PUT /delivery/update/{id_}`: Update an existing delivery.
- `DELETE /delivery/delete/{id_}`: Delete a delivery.
- `GET /delivery/get_by_id/{id_}`: Get a delivery by ID.
- `GET /delivery/get_all`: Get all deliveries.

### Favorite List User Product

- `POST /favorite_list_user_product/create`: Create a new favorite list user product.
- `PUT /favorite_list_user_product/update/{id_}`: Update an existing favorite list user product.
- `DELETE /favorite_list_user_product/delete/{id_}`: Delete a favorite list user product.
- `GET /favorite_list_user_product/get_by_id/{id_}`: Get a favorite list user product by ID.
- `GET /favorite_list_user_product/get_all`: Get all favorite list user products.

### Favorite List User Store

- `POST /favorite_list_user_store/create`: Create a new favorite list user store.
- `PUT /favorite_list_user_store/update/{id_}`: Update an existing favorite list user store.
- `DELETE /favorite_list_user_store/delete/{id_}`: Delete a favorite list user store.
- `GET /favorite_list_user_store/get_by_id/{id_}`: Get a favorite list user store by ID.
- `GET /favorite_list_user_store/get_all`: Get all favorite list user stores.

### Payment Method

- `POST /payment_method/create`: Create a new payment method.
- `PUT /payment_method/update/{id_}`: Update an existing payment method.
- `DELETE /payment_method/delete/{id_}`: Delete a payment method.
- `GET /payment_method/get_by_id/{id_}`: Get a payment method by ID.
- `GET /payment_method/get_all`: Get all payment methods.

### Receipt

- `POST /receipt/create`: Create a new receipt.
- `PUT /receipt/update/{id_}`: Update an existing receipt.
- `DELETE /receipt/delete/{id_}`: Delete a receipt.
- `GET /receipt/get_by_id/{id_}`: Get a receipt by ID.
- `GET /receipt/get_all`: Get all receipts.

### Shopping Cart

- `POST /shopping_cart/create`: Create a new shopping cart.
- `PUT /shopping_cart/update/{id_}`: Update an existing shopping cart.
- `DELETE /shopping_cart/delete/{id_}`: Delete a shopping cart.
- `GET /shopping_cart/get_by_id/{id_}`: Get a shopping cart by ID.
- `GET /shopping_cart/get_all`: Get all shopping carts.

### Status Cart

- `POST /status_cart/create`: Create a new status cart.
- `PUT /status_cart/update/{id_}`: Update an existing status cart.
- `DELETE /status_cart/delete/{id_}`: Delete a status cart.
- `GET /status_cart/get_by_id/{id_}`: Get a status cart by ID.
- `GET /status_cart/get_all`: Get all status carts.

## Entities

- **User**: Manages user information.
- **Product**: Manages product details.
- **Cart**: Manages shopping cart details.
- **Order**: Manages order details.
- **Payment**: Manages payment details.
- **Category**: Manages product categories.
- **Review**: Manages product reviews.
- **Address**: Manages user addresses.
- **Store**: Manages store details.
- **Transaction Status**: Manages transaction statuses.
- **Status Report**: Manages status reports.
- **Category Report**: Manages category reports.
- **Client Report**: Manages client reports.
- **Delivery**: Manages delivery details.
- **Favorite List User Product**: Manages favorite list user products.
- **Favorite List User Store**: Manages favorite list user stores.
- **Payment Method**: Manages payment methods.
- **Receipt**: Manages receipts.
- **Shopping Cart**: Manages shopping cart details.
- **Status Cart**: Manages status carts.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.