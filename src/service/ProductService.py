from src.model.product.Product import Product
from src.repository.dao.ProductDao import ProductDao


class ProductService:
    def __init__(self, product_dao: ProductDao):
        self.__product_dao = product_dao

    def get_product(self) -> Product:
        product: Product = self.__product_dao.get_any()
        return product
