import pymongo


class ItemHandler:

    """
    Mixin for dealing with items from a specific foo.bar database.
    """

    bar_collection: pymongo.collection.Collection

    def get_db_item(self):
        return self.bar_collection.find_one()


class MongoDB(ItemHandler):
    def __init__(self):
        self.client = None

    def init_from_app(self, app):
        """
        Set up a mongoclient using app.config
        """
        mongo_uri = app.config["MONGO_URI"]
        self.client = self._get_mongo_client(mongo_uri)
        self.bar_collection = self.client["foo"]["bar"]

    def _get_mongo_client(self, mongo_uri):
        """
        This function will be mocked in testing and modified
        to return a mongomock.MongoClient instead.
        """
        return pymongo.MongoClient(mongo_uri)
