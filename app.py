from flask import Flask
from db import MongoDB

mongo = MongoDB()


def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "localhost:27017"
    app.config["DEBUG"] = True
    mongo.init_from_app(app)

    # Add example route:
    @app.route("/foo")
    def view_db_item():
        """
        Serve db item via a getter function
        """
        item = mongo.get_db_item()
        return str(item)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
