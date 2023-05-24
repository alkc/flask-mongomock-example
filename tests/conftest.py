import pytest
import mongomock
import pytest_mock as mocker
from app import create_app


@pytest.fixture()
def app(mocker, mock_database_client):  # noqa: F811
    """Return app connected to mock database"""  
    mock_mongo = mocker.patch("app.mongo._get_mongo_client")
    # the internal _get_mongo_client function is modified below to return the pre-configured
    # mongomock.MongoClient, instead of trying to initialize and return a pymongo.MongoClient
    # the MongoDB object will be initialized with the mongomock.MongoClient, when create_app
    # is called below.
    mock_mongo.return_value = mock_database_client

    app = create_app()
    app.config["TESTING"] = True

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def database_item():
    """Mock db item"""
    item = {"foo": "bar"}

    return item


@pytest.fixture()
def mock_database_client(database_item):
    """
    Populated mock db
    
    This mock client will repleace the real pymongo client
    when running the tests.
    """
    client = mongomock.MongoClient()
    # Insert one example object:
    client["foo"]["bar"].insert_one(database_item)

    return client
