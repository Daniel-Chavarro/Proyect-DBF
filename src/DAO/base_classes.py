from typing import Optional, List
from datetime import datetime
from DAO.base_model import ProjectModel

class UserData(ProjectModel):
    id_user: int = -1
    id_address_fk: int
    id_account_status_fk: int = 1
    id_type_user_fk: int = 1
    name: str
    last_name: str
    username: str
    email: str
    phone: str
    date_birth: str
    date_register: str
    password: str
    status: Optional[str]
    role: Optional[str]
    country: Optional[str]
    city: Optional[str]

class TypeUserData(ProjectModel):
    id_type_user: int = -1
    name: str
    description: Optional[str]

class StatusCartData(ProjectModel):
    id_status_cart: int = -1
    name: str
    description: Optional[str]

class AccountStatusData(ProjectModel):
    id_account_status: int = -1
    name: str
    description: Optional[str]

class ProductData(ProjectModel):
    id_product: int = -1
    id_store_fk: int
    id_product_status_fk: int
    id_category_fk: int
    id_brand_fk: int
    name: str
    description: Optional[str]
    price: float
    stock: Optional[int] = 0
    date_published: str
    rating: Optional[float] = 0.0
    # Added nested objects
    store: Optional['StoreData'] = None
    status: Optional['ProductStatusData'] = None
    category: Optional['CategoryProductData'] = None
    brand: Optional['BrandData'] = None

class StoreData(ProjectModel):
    id_store: int = -1
    id_user_fk: int
    id_address_fk: int
    name: str
    description: Optional[str]
    phone: str
    email: str
    date_created: str
    # Added nested objects
    owner: Optional['UserData'] = None
    address: Optional['AddressData'] = None
    products: List['ProductData'] = []

class AddressData(ProjectModel):
    id_address: int = -1
    street: str
    city: str
    state: str
    country: str
    zip_code: str

class BrandData(ProjectModel):
    id_brand: int = -1
    name: str
    description: Optional[str]

class CategoryProductData(ProjectModel):
    id_category: int = -1
    name: str
    description: Optional[str]

class ProductStatusData(ProjectModel):
    id_product_status: int = -1
    name: str
    description: Optional[str]

class DeliveryProviderData(ProjectModel):
    id_delivery_provider: int = -1
    name: str
    phone: str
    email: Optional[str]
    description: Optional[str]

class DeliveryData(ProjectModel):
    id_delivery: int = -1
    id_user_fk: int
    id_shopping_cart_fk: int
    id_delivery_provider_fk: int
    id_delivery_status_fk: int
    id_address_fk: int
    date_created: str
    date_estimated_arrive: str
    delivery_cost: float
    # Added nested objects
    user: Optional['UserData'] = None
    shopping_cart: Optional['ShoppingCartData'] = None
    provider: Optional['DeliveryProviderData'] = None
    status: Optional['DeliveryStatusData'] = None
    address: Optional['AddressData'] = None

class DeliveryStatusData(ProjectModel):
    id_delivery_status: int = -1
    name: str
    description: Optional[str]

class ShoppingCartData(ProjectModel):
    id_shopping_cart: int = -1
    id_status_cart_fk: int
    id_user_fk: int
    date_created: str
    total: float = 0.0
    # Added nested objects
    status: Optional[str] = None
    items: List['CartItemData'] = []
    delivery: Optional['DeliveryData'] = None

class CartItemData(ProjectModel):
    id_cart_item: int = -1
    id_shopping_cart_fk: int
    id_product_fk: int
    quantity: int
    subtotal: float
    # Added nested object
    product: Optional['ProductData'] = None

class FavoriteListUserStoreData(ProjectModel):
    id_favorite_store: int = -1
    id_user_fk: int
    id_store_fk: int
    date_created: str
    name: str

class FavoriteListUserProductData(ProjectModel):
    id_favorite_product: int = -1
    id_user_fk: int
    id_product_fk: int
    date_created: str
    name: str

class ReceiptData(ProjectModel):
    id_receipt: int = -1
    id_shopping_cart_fk: int
    id_payment_method_fk: int
    id_transaction_status_fk: int
    date_created: str
    total: float

class PaymentMethodData(ProjectModel):
    id_payment_method: int = -1
    name: str
    description: Optional[str]

class TransactionStatusData(ProjectModel):
    id_transaction_status: int = -1
    name: str
    description: Optional[str]

class ClientReportData(ProjectModel):
    id_client_report: int = -1
    id_user_reporter_fk: int
    id_user_reported_fk: int
    id_category_report_fk: int
    id_status_report_fk: int
    description: str
    date_created: str

class CategoryReportData(ProjectModel):
    id_category_report: int = -1
    name: str
    description: Optional[str]

class StatusReportData(ProjectModel):
    id_status_report: int = -1
    name: str
    description: Optional[str]

class FavoriteListUserProductData(ProjectModel):
    id_favorite_product: int = -1
    id_user_fk: int
    id_product_fk: int
    date_added: str


