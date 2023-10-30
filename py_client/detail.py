import requests
import json
 
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": 'Remote',
    "price": 800
    
}

# headers =  {'Content-Type': 'application/json; charset=utf-8'}
get_response = requests.post(endpoint, json=data)

print(get_response.json())