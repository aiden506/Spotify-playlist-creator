import requests
import base64
import datetime

# Class To Get OAuth Token
class SpotifyAPIToken:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_creds = None
        self.client_creds_b64 = None
        self.url = 'https://accounts.spotify.com/api/token'

    def GetClientCredentials(self):
        self.client_creds = f"{self.client_id}:{self.client_secret}"
        self.client_creds_b64 = base64.b64encode(self.client_creds.encode())
        return self.client_creds_b64
    
    def TokenRequest(self):
        client_creds_b64 = self.GetClientCredentials()
        response = requests.post(self.url, data={'grant_type': 'client_credentials'}, 
        headers={'Authorization': f"Basic {client_creds_b64.decode()}"})
        if response.status_code is 200:
            print('Token Acquiring Successful', '\n')
        else:
            print('Token Acquiration Failed')
            exit(1)
        token_response_data = response.json()
        access_token = token_response_data['access_token']
        print('Your access token:', access_token)

# Getting Access Token
client_id = '1906ff01f5ee4766aa640a9fbb4e6207'
client_secret = '3d6e7c5ca8224f61bedddf4b6e03412d'
Spotify = SpotifyAPIToken(client_id, client_secret)
Spotify.TokenRequest()