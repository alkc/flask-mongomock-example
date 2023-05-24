def test_db_views_1(app):
    with app.test_client() as client:
        response = client.get("/foo1")
        assert response.status_code == 200
        assert b'foo' in response.data

def test_db_views_2(app):
    with app.test_client() as client:
        response = client.get("/foo2")
        assert response.status_code == 200
        assert b'foo' in response.data
