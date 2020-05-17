from pymongo import MongoClient


class Mongo:
    def __init__(self, host: str, port: int, default_db: str):
        self.__client = MongoClient(
            host=host,
            port=port
        )
        self.__database = self.__client[default_db]

    def find_all(self, collection: str):
        db_collection = self.__database[collection]
        for elem in db_collection.find():
            yield elem

    def find_by(self, collection: str, field: dict):
        db_collection = self.__database[collection]
        for elem in db_collection.find(field):
            yield elem

    def get_any(self, collection: str):
        db_collection = self.__database[collection]
        for elem in db_collection.aggregate([{'$sample': {'size': 1}}]):
            return elem


if __name__ == '__main__':
    mongo = MongoClient(
        host="localhost",
        port=27017
    )
    db = mongo["productCatalog"]
    collection = db["productCatalog"]

    for elem in collection.aggregate([{'$sample': {'size': 1}}]):
        print(elem)
