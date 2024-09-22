import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

# target_year = input("When would you like to travel to (YYYY-MM-DD)?\n")
target_year = "1997-10-07"
BASE_URL = "https://www.billboard.com/charts/hot-100/"
full_url = BASE_URL + target_year + "/"

request = requests.get(url=full_url)
request.raise_for_status()

top_song = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet"
other_songs = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"

soup = BeautifulSoup(request.text, "html.parser")
chart_results = soup.find("div", class_="chart-results-list")
best_song = chart_results.find("h3", {"id": "title-of-a-story", "class":top_song})
songs = chart_results.find_all("h3", {"id":"title-of-a-story", "class": other_songs})

# print(songs)
song_list = []

for song_idx in range(len(songs)):
    if song_idx == 0:
        song_list.append(best_song.text.strip())
    song_list.append(songs[song_idx].text.strip())

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIFY_CLIENT"),
                                               client_secret=os.getenv("SPOTIFY_SECRET"),
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private"))

user_id = sp.current_user()["id"]

spotify_responses = []
for song in song_list:
    query = f"track: {song} year: {target_year.split('-')[0]}"
    try:
        resp = sp.search(song, limit=1)
    except:
        print(f"Song: {song} unavailable, skipping")
    spotify_responses.append(resp)

spotify_uri_list = []
for resp_idx in range(len(spotify_responses)):
    tmp_dict = spotify_responses[resp_idx]
    local_uri = tmp_dict['tracks']["items"][0]['uri']
    spotify_uri_list.append(local_uri)

playlist_name = target_year + " Billboard 100"
playlist = sp.user_playlist_create(user_id, playlist_name, public=False, collaborative=False, description="python project")

sp.user_playlist_add_tracks(user_id, playlist["id"], spotify_uri_list)
