
import pytest
from fastapi.testclient import TestClient
from division import divide_numbers
from main import app

client = TestClient(app)


def test_normal_division():
    assert divide_numbers(20, 5) == 4


def test_numerator_smaller():
    assert divide_numbers(10, 20) == 0.5


def test_division_by_zero():
    with pytest.raises(ValueError):
        divide_numbers(10, 0)


def test_api_division():
    response = client.post(
        "/divide",
        json={"num": 20, "denominator": 5}
    )

    assert response.status_code == 200
    assert response.json()["result"] == 4.0


def test_api_zero_denominator():
    response = client.post(
        "/divide",
        json={"num": 10, "denominator": 0}
    )

    assert response.status_code == 400
