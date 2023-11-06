import requests
import json
 
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/"



# headers =  {'Content-Type': 'application/json; charset=utf-8'}
get_response = requests.get(endpoint)

print(get_response.json())