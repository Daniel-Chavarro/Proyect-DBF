"""This module is the entry point of the application.

It contains the FastAPI instance and the routers
that will be used in the application.

Author: Carlos Andres Sierra <cavirguezs@udistrital.edu.co>
"""

from fastapi import FastAPI, HTTPException

from services import (
    users_router,
    address_router,
    brand_router,
    cart_router,
    category_product_router,
    category_report_router,
    client_report_router,
    delivery_router,
    delivery_provider_router,
    favorite_list_user_product_router,
    favorite_list_user_store_router,
    payment_method_router,
    product_router,
    product_status_router,
    receipt_router,
    shopping_cart_router,
    status_cart_router,
    status_report_router,
    store_router,
    transaction_status_router,
    type_user_router,

)

app = FastAPI(
    title="Football API",
    version="0.0.1",
    description="This is an example of a CRUD using services for a football tournament.",
)


app.include_router(users_router)
app.include_router(address_router)
app.include_router(brand_router)
app.include_router(cart_router)
app.include_router(category_product_router)
app.include_router(category_report_router)
app.include_router(client_report_router)
app.include_router(delivery_router)
app.include_router(delivery_provider_router)
app.include_router(favorite_list_user_product_router)
app.include_router(favorite_list_user_store_router)
app.include_router(payment_method_router)
app.include_router(product_router)
app.include_router(product_status_router)
app.include_router(receipt_router)
app.include_router(shopping_cart_router)
app.include_router(status_cart_router)
app.include_router(status_report_router)
app.include_router(store_router)
app.include_router(transaction_status_router)
app.include_router(type_user_router)
    

@app.get("/")
async def root():
    """This method is used to get the root of the API."""
    return {"message": "Welcome to the Football API!"}