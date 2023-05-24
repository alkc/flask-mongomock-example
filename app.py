from flask import Flask
from db import MongoDB

mongo = MongoDB()


def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "localhost:27017"
    app.config["DEBUG"] = True
    mongo.init_from_app(app)

    @app.route("/foo1")
    def view_db_item():
        """
        Serve db item via getter function
        """
        item = mongo.get_db_item()
        return str(item)

    @app.route("/foo2")
    # ‘/’ URL is bound with hello_world() function.
    def view_db_item2():
        """
        Serve db item directly from collection
        """
        item = mongo.bar_collection.find_one()
        return str(item)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
