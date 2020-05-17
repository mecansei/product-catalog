import os

from src.library.database.Mongo import Mongo
from src.model.product.Product import Product


class ProductDao:
    def __init__(self):
        self.__mongo: Mongo = Mongo(
            host=os.getenv("MONGO_HOST"),
            port=int(os.getenv("MONGO_PORT")),
            default_db=os.getenv("MONGO_DEFAULT_DB")
        )
        self.__collection = "productCatalog"

    def get_any(self) -> Product:
        elem = self.__mongo.get_any(
            collection=self.__collection
        )

        return self.__build_product(elem)

    @staticmethod
    def __build_product(elem) -> Product:
        return Product(
            name=elem["name"],
            photos=elem["photos"],
            value=elem["value"],
            size=elem["size"],
            brand=elem["brand"],
            description=elem["description"],
            color=elem["color"]
        )
