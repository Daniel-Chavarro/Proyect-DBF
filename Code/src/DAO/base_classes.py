from DAO.base_model import ProjectModel

class UserData(ProjectModel):
    id_user: int = -1
    name:str
    last_name: str
    username: str
    email: str
    phone: str
    date_birth: str
    date_register: str
    password: str
    is_active: bool
    is_superuser: bool = False

class Product:
    id_product: int = -1
    id_store_fk: int
    id_product_status_fk: int
    name: str
    description: str
    price: float
    stock: int
    category: str
    
