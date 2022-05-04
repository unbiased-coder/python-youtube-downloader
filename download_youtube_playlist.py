import os
from pytube import Playlist
from dotenv import load_dotenv

load_dotenv()
playlist_location = os.getenv('YOUTUBE_PLAYLIST')
playlist_obj = Playlist(playlist_location)
for video in playlist_obj.videos:
    r = video.streams.first().download()
    print('Downloaded: ', r)
