import requests
import json
 
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"querry":"Hello World"})
print(get_response.text)
# print(json.loads('{"querry":"12"}'))
# print(get_response.text)
print(get_response.json())