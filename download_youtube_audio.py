import os
import pprint

from pytube import YouTube
from dotenv import load_dotenv

load_dotenv()
video_location = os.getenv('YOUTUBE_VIDEO')
yt_obj = YouTube(video_location)
yt_stream = yt_obj.streams.filter(only_audio=True, mime_type='audio/mp4')
if yt_stream:
    yt_stream = yt_stream[0]

print (f'Found stream:\nNAME: {yt_stream.title}\nBITRATE: {yt_stream.abr}\nTYPE: {yt_stream.subtype}')
print ('Starting to download, please wait...')
r = yt_stream.download()
print ('File saved: ', r)
