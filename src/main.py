from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers from service files
from services.users import router as user_router
from services.product import router as product_router
from services.cart import router as cart_router
from services.category_product import router as category_router
from services.address import router as address_router
from services.store import router as store_router
from services.transaction_status import router as transaction_status_router
from services.status_report import router as status_report_router
from services.category_report import router as category_report_router
from services.client_report import router as client_report_router
from services.delivery import router as delivery_router
from services.favorite_list_user_product import router as favorite_list_user_product_router
from services.favorite_list_user_store import router as favorite_list_user_store_router
from services.payment_method import router as payment_method_router
from services.receipt import router as receipt_router
from services.shopping_cart import router as shopping_cart_router
from services.status_cart import router as status_cart_router

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user_router, prefix="/api/v1")
app.include_router(product_router, prefix="/api/v1")
app.include_router(cart_router, prefix="/api/v1")
app.include_router(category_router, prefix="/api/v1")
app.include_router(address_router, prefix="/api/v1")
app.include_router(store_router, prefix="/api/v1")
app.include_router(transaction_status_router, prefix="/api/v1")
app.include_router(status_report_router, prefix="/api/v1")
app.include_router(category_report_router, prefix="/api/v1")
app.include_router(client_report_router, prefix="/api/v1")
app.include_router(delivery_router, prefix="/api/v1")
app.include_router(favorite_list_user_product_router, prefix="/api/v1")
app.include_router(favorite_list_user_store_router, prefix="/api/v1")
app.include_router(payment_method_router, prefix="/api/v1")
app.include_router(receipt_router, prefix="/api/v1")
app.include_router(shopping_cart_router, prefix="/api/v1")
app.include_router(status_cart_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Project DBF API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)