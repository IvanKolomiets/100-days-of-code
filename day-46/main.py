import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
# 2000-08-12
URL = 'https://www.billboard.com/charts/hot-100'
SPOTIFY_CLIENT_ID = os.environ('CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ('CLIENT_SECRET')

date_string = input('Which year dp you want travel to? Type the date in this format YYYY-MM-DD:')
response = requests.get(f"{URL}/{date_string}")
soup = BeautifulSoup(response.text,'html.parser')
song_list = [''.join(x.text.split()) for x in soup.select(selector="li h3[id=title-of-a-story]")]


#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(f'id - {user_id}')

song_uris = []
year = date_string.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except:
        print(f"{song} doesn't exist in Spotify, will skip")

playlist = sp.user_playlist_create(user=user_id, name=f"{date_string} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)