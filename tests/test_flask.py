import pytest
from backPDD import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_config():
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_base(client):
    response = client.get("/")
    assert response.data == b"Hola Maxi y Gustavo!"
