def test_db_view(app):
    with app.test_client() as client:
        response = client.get("/foo")
        assert response.status_code == 200
        assert b"foo" in response.data

