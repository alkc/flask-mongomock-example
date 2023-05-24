import pytest
import mongomock
import pytest_mock as mocker
from app import create_app


@pytest.fixture()
def app(mocker, mock_database_client):  # noqa: F811
    """Return empty app"""

    mock_mongo = mocker.patch("app.mongo._get_mongo_client")
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
    """Populated mock db"""
    client = mongomock.MongoClient()
    client["foo"]["bar"].insert_one(database_item)

    return client
