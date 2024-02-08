import pytest
from app import create_app
from app.extensions import db
from flask_jwt_extended import create_access_token

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app
    with app.app_context():
        db.drop_all()

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

@pytest.fixture()
def jwt_token(app):
    with app.app_context():
        return create_access_token(identity="email@gmail.com")