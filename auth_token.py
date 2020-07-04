import requests
import json
import os
import base64
import datetime

username = 'aiden'
client_id = '10646c5a2aa945cba3bdc3b2504bbc08'
client_secret = '92f06c4f9d6042aabbe5c380ca91cc4c'


#a class to be added here


client_creds = f"{client_id}:{client_secret}"

client_creds_b64 = base64.b64encode(client_creds.encode())

token_url = "https://accounts.spotify.com/api/token"

method = "POST"
token_data = {
    "grant_type": "client_credentials"

}
token_headers = {
    "Authorization": f"Basic {client_creds_b64.decode()}"

}

r = requests.post(token_url, data=token_data, headers=token_headers)
print(r.json())                       #Prints out the access token
valid_request = r.status_code in range(200, 299)

if valid_request:
    token_response_data = r.json()
    present = datetime.datetime.now()
    access_token = token_response_data['access_token']
    expires_in = token_response_data['expires_in']
    expires = present + datetime.timedelta(seconds=expires_in)
    expired = expires < present
