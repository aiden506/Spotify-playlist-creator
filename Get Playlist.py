import requests
import base64
import json
from urllib.parse import urlencode

# USER CREDENTIALS
client_id = '1906ff01f5ee4766aa640a9fbb4e6207'
client_secret = '627fb88c2eac4d288795e96b180603a4'

# Class To Get OAuth Token
class SpotifyAPIToken:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_creds = None
        self.client_creds_b64 = None
        self.token_url = 'https://accounts.spotify.com/api/token'

    def GetClientCredentials(self):
        self.client_creds = f"{self.client_id}:{self.client_secret}"
        self.client_creds_b64 = base64.b64encode(self.client_creds.encode())
        return self.client_creds_b64
    
    def TokenRequest(self):
        client_creds_b64 = self.GetClientCredentials()
        token_response = requests.post(self.token_url, data={
            'grant_type': 'client_credentials'
            }, 
        headers={
            'Authorization': f"Basic {client_creds_b64.decode()}", 
            })
        if token_response.status_code in range(200, 299):
            print('Token Acquisition Successful', '\n')
        else:
            print('Token Acquisition Failed')
            exit(1)
        token_response_data = token_response.json()
        access_token = token_response_data['access_token']
        return access_token

class GetPlaylist(SpotifyAPIToken):
    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)
        self.url = 'https://api.spotify.com/v1/search'
        self.playlist_name = None
        self.data = urlencode({
        'q': "Don't Wanna Lose You", # playlist name to search for
        'type': 'playlist', 
        'limit': 50 # number of results to retrieve (50 is upper limit)
        })
        # Getting Access Token
        self.access_token = self.TokenRequest()
        self.headers = {
            'Authorization': f"Bearer {self.access_token}"
        }
        self.real_url = f"{self.url}?{self.data}"
    
    # Get Playlist Name
    def USER_INPUT(self):
        self.playlist_name = str(input('Enter the name of the playlist you wish to search for: '))
        return self.playlist_name
    
    def Get_Playlist(self):
        self.USER_INPUT()
        get_playlist_response = requests.get(self.real_url, headers=self.headers)
        for x in get_playlist_response.json()['playlists']['items']: # this part is not intuitive
            print('Playlist Name:', x['name'])                       # you have to go through the .json file
            print('Playlist Creator:', x['owner']['display_name'])   # to see how the lists are arranged to
            print('\n')                                              # write this stuff

GP = GetPlaylist(client_id, client_secret)
GP.Get_Playlist()
