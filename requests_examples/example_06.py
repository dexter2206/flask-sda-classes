import json
import requests

URL = "http://localhost:5000/json"


if __name__ == "__main__":
    data = {"foo": "bar", "baz": 10}
    response = requests.post(URL, data=json.dumps(data))
    print(response.status_code)

    response = requests.post(
        URL, data=json.dumps(data), headers={"content-type": "application/json"}
    )
    print(response.status_code)

    response = requests.post(URL, json=data)
    print(response.status_code)
