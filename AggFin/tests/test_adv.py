import pytest
from AggFin import create_app, db
from AggFin.models import User

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_register_user(client):
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass123'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Your account has been created!' in response.data

def test_login_invalid(client):
    response = client.post('/login', data={
        'email': 'wrong@example.com',
        'password': 'wrongpass'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Login failed' in response.data

def test_stock_search_post(client):
    response = client.post('/home', data={'stock_name': 'AAPL'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'AAPL' in response.data or b'Stock Information' in response.data
