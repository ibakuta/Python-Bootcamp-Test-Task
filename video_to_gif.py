import requests
from moviepy.editor import VideoFileClip
import wget
import os

def video_to_gif():
    url = str(input("Please give me url: "))

    filename = wget.download(url)
    clip = VideoFileClip(filename)
    clip = clip.subclip(0, 3)
    clip.write_gif("my-life.gif")

    return os.path.abspath(r"my-life.gif")

print(video_to_gif())