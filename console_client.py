import requests

url = 'http://127.0.0.1:8000/api/'

# GET
response = requests.get(url)
print(response.status_code)
# print(response.headers)
print(response.json())
