import pytest
import mongomock
import pytest_mock as mocker
from app import create_app


@pytest.fixture()
def app(mocker, mock_database_client):  # noqa: F811
    """Return empty app"""

    mock_mongo = mocker.patch("app.mongo")
    mock_mongo.init_from_app.return_value = None

    mock_mongo.client = mock_database_client
    mock_mongo.bar_collection = mock_database_client["foo"]["bar"]

    app = create_app()
    app.config["TESTING"] = True

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def database_item():

    item = {"foo": "bar"}

    return item


@pytest.fixture()
def mock_database_client(database_item):

    client = mongomock.MongoClient()
    client["foo"]["bar"].insert_one(database_item)

    return client
