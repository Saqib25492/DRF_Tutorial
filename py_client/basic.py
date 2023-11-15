import requests
import json
from getpass import getpass
 
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/gettoken/"
username = input("Enter Your Username: ")
password = getpass()
# data = {
#     'title':'Wood',
#     'content':'Woolen Sweater',
  
# }


# json_data = json.dumps(data)
# print(json_data)
 
headers =  {'Content-Type': 'application/json; charset=utf-8'}
auth_response = requests.post(endpoint, json={"username":username, "password":password})
    
if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f"Token {token}",
    }
    endpoint = "http://127.0.0.1:8000/api/products/"
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())

# upload_data = requests.post(endpoint, data=json_data, headers=headers)
# print(upload_data.json())                                       
# print(get_response.text, "text")
# print(json.loads('{"querry":"12"}')) 
# print(get_response.text)
# print(get_response.json(), "json")