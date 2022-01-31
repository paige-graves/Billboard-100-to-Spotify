import requests
import spotipy
from bs4 import BeautifulSoup

desired_date = input("What date would you like to search for? Type the date in YYYY-MM-DD format.")

URL = f"https://www.billboard.com/charts/hot-100/{desired_date}/"

response = requests.get(URL)
top_100_webpage = response.text

soup = BeautifulSoup(top_100_webpage, "html.parser")

song_reference = soup.find_all(name="li", class_="lrv-u-width-100p")


all_songs = []

for element in song_reference:
    song_titles = element.find(name="h3", class_="c-title")
    if song_titles is None:
        pass
    else:
        all_songs.append(song_titles.getText())

all_songs = [song.strip("\n") for song in all_songs]

## ------ From Spotify API ------- ##
CLIENT_ID = "Insert Client ID"
CLIENT_SECRET = "Insert Client Secret"
SPOTIPY_REDIRECT_URI = "http://example.com"
## ----- Needed to create a private playlist in Spotify ----- ##
SCOPE = 'playlist-modify-private'

## To authenticate in Spotify ##
sp = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE)
client_credentials = spotipy.client.Spotify(client_credentials_manager=sp)
USER_CREDENTIALS = client_credentials.current_user()['id']

## Adding songs by URI ##
SPOTIFY_SONG_URIS = []
PLAYLIST_NAME = f"Billboard Top 100 {desired_date}"

for n in range(100):
    song_uri_search = client_credentials.search(q=f"track:{all_songs[n]} year:{desired_date[0:4]}")
    try:
        SPOTIFY_SONG_URIS.append(song_uri_search['tracks']['items'][0]['uri'])
    except IndexError:
        print(f"{all_songs[n]} couldn't be found. Skipped.")

## ---- Adding to playlist ---- ##
NEW_PLAYLIST = client_credentials.user_playlist_create(user=USER_CREDENTIALS, name=PLAYLIST_NAME, public=False)
NEW_PLAYLIST_ID = NEW_PLAYLIST['id']

client_credentials.playlist_add_items(playlist_id=NEW_PLAYLIST_ID, items=SPOTIFY_SONG_URIS)



