import requests

BASE_URL = "http://localhost:5000"


def test_home_endpoint():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200


def test_db_check_endpoint():
    response = requests.get(f"{BASE_URL}/db-check")
    assert response.status_code == 200


def test_menu_endpoint():
    response = requests.get(f"{BASE_URL}/menu")
    assert isinstance(response.json(), list)
