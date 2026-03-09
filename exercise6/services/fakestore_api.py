import requests

response = requests.get('https://fakestoreapi.com/products/1')
print(response.json())