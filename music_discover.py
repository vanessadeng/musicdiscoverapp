from flask import Flask, redirect, request,session
from dotenv import load_dotenv
import requests
import os
import sys
import json
load_dotenv()
CLIENT_ID = os.getenv('SPOTFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World"

@app.route('/get_auth')
def request_auth():
    """Request user authorization from spotify."""
    scope = 'user-top-read playlist-modify-public playlist-modify-private user-follow-read'
    return redirect(f'https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={scope}')


@app.route('/callback')
def request_token():
    code = requests.args.get('code')

    payload = {
        'grant_type':'authorization',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id':CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    r = requests.post(SPOTIFY_TOKEN_URL,data=payload)
    response = r.json()

    tokens = {
        'access_token': response['access_token'],
        'refresh_token': response['refresh_token'],
        'expires_in': response['expires_in']
    }
    with open('tokens.json','w') as outfile:
        json.dump(tokens,outfile)
    return "successfully completed auth flow"

    

if __name__ == '__main__':
    app.run()