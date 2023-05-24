import pymongo

class FooHandler:

    bar_collection : pymongo.collection.Collection

    def get_db_item(self):
        return self.bar_collection.find_one()


class MongoDB(FooHandler):

    def __init__(self):
        self.client = None

    def init_from_app(self, app):

        mongo_uri = app.config['MONGO_URI']
        self.client = pymongo.MongoClient(mongo_uri)
        self.bar_collection = self.client['foo']['bar']

        
