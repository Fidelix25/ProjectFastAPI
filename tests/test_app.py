from http import HTTPStatus

from fastapi.testclient import TestClient

from projectfastapi.app import app


def test_root_return_hello_world():
    """
    Three step  (AAA)
    - A: Arrange
    - A: Act
    - A: Assert
    """
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Hello World!'}
    assert response.status_code == HTTPStatus.OK
