# Testing a pymongo/Flask app using pytest and mongomock

This repo contains an example on how to use mongomock to replace a `pymongo.MongoClient` inside a Flask app.

The dependencies, test cases, and structure of the app are based on a real project where I was scratching my head over this exact problem.

The setup of the `db.MongoDB` class imported and initialized in app.py is based on the MongoAdapter in [Clinical-Genomics/scout](https://github.com/Clinical-Genomics/scout/blob/main/scout/adapter/mongo/base.py)

To try it out, clone this repo, install the dependencies in `requirements.txt` and run pytest:

``` python
git clone https://github.com/alkc/flask-mongomock-example.git
cd flask-mongomock-example
pip install --requirement requirements.txt
pytest .
```

I'm open for feedback if you think there is a smarter/better way of doing this.
