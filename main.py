#!/usr/bin/env python3

from typing import Dict, Tuple, List

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

def get_app_info(filename='keys.txt') -> Dict[str, str]:
    output: Dict[str, str] = {}
    with open(filename, mode='r') as f:
        output['public'] = f.readline()
        output['secret'] = f.readline()
        output['website'] = f.readline()
        output['redirect'] = f.readline()
    return output

# More info - https://developer.spotify.com/documentation/web-api/reference/player/get-recently-played/

app_info: Dict[str, str] = get_app_info()

scopes = 'user-read-recently-played playlist-modify-public'

authority = SpotifyOAuth(client_id=app_info['public'], client_secret=app_info['secret'], redirect_uri=app_info['redirect'], scope=scopes, cache_path='./.cache/')
client_creds = SpotifyClientCredentials(client_id=app_info['public'], client_secret=app_info['secret'])

sp = spotipy.Spotify(auth_manager=authority)

results = sp.search(q='weezer', limit=20)
for index, track in enumerate(results['tracks']['items']):
    print(f'{index}: {track["name"]}')

