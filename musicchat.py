from chatterbot import ChatBot
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import os

# Set up Spotify client credentials
client_id = os.getenv("SPOTIFY_CLIENT_ID")  # Set your Spotify client ID here
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")  # Set your Spotify client secret here
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Initialize ChatBot
bot = ChatBot("MusicBot")

# Function to search for a song on Spotify
def search_song(query):
    results = sp.search(q=query, type="track", limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return track['name'], track['preview_url']
    else:
        return None, None

# Function to handle user requests
def handle_request(user_input):
    response = bot.get_response(user_input)
    if "play" in user_input:
        song_name = user_input.replace("play", "").strip()
        song, preview_url = search_song(song_name)
        if song and preview_url:
            return f"Sure, here's a preview of '{song}': {preview_url}"
        else:
            return "Sorry, I couldn't find that song."
    else:
        return response

# Main loop
print("Welcome to Music ChatBot! You can request songs to listen to.")
print("Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = handle_request(user_input)
    print("Bot:", response)
