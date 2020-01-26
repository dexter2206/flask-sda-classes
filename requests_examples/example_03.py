import requests

URL = "http://localhost:5000/hello2"


if __name__ == "__main__":
    response = requests.get(URL, params={"name": "Konrad Jałowiecki"})
    print(response.text)

