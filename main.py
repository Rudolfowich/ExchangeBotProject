import requests
from settings import access_key

url = 'http://api.exchangeratesapi.io/v1/latest?access_key=1f6d34cfc2196de962109fe38ec5fe5d'
res = requests.get(url)
print(res.text)
