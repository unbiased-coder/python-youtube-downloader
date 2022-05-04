import os

from pytube import YouTube
from dotenv import load_dotenv

load_dotenv()
video_location = os.getenv('YOUTUBE_VIDEO')
yt_obj = YouTube(video_location)
yt_stream = yt_obj.streams.get_highest_resolution()
print (f'Found stream:\nNAME: {yt_stream.title}\nRES: {yt_stream.resolution}\nFPS: {yt_stream.fps}\nTYPE: {yt_stream.subtype}')
print ('Starting to download, please wait...')
r = yt_stream.download()
print ('File saved: ', r)
