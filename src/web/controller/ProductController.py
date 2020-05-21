from flask import Blueprint
from flask_cors import cross_origin

from src.model.product.Product import Product
from src.repository.dao.ProductDao import ProductDao
from src.service.ProductService import ProductService
from src.web.controller.UtilController import UtilController

product_controller = Blueprint('ProductController', __name__)

product_dao: ProductDao = ProductDao()

service: ProductService = ProductService(
    product_dao=product_dao
)


class ProductController:
    @staticmethod
    @cross_origin()
    @product_controller.route('/product/', methods=['GET'])
    def get():
        response: dict
        status_code: int = 200
        try:
            product: Product = service.get_product()
            response = product.__dict__
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)
