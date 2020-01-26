import requests


ADDRESS = "http://localhost:5000"


if __name__ == "__main__":
    # Test /both path
    response = requests.get(ADDRESS + "/both")
    assert response.status_code == 200

    response = requests.post(ADDRESS + "/both")
    assert response.status_code == 200

    # Test /get path
    response = requests.get(ADDRESS + "/get")
    assert response.status_code == 200

    response = requests.post(ADDRESS + "/get")
    assert response.status_code == 405

    # Test /post path
    response = requests.get(ADDRESS + "/post")
    assert response.status_code == 405

    response = requests.post(ADDRESS + "/post")
    assert response.status_code == 200
