import csv
import os 
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

def download_song(title, artist):
    query = f"{title} {artist}"
    return "nya!"

download_song()

# ydl_opts = {'format': 'bestaudio'}
# with YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc']) 