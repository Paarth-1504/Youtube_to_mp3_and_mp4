import shutil
import time

from moviepy.editor import *
from pytube import YouTube

errors = 0 # its a counter variable to keep track of any errors


def download_files(url):
    global errors

    try:
        mp4 = YouTube(url).streams.get_highest_resolution().download()
        mp3 = mp4.split(".mp4", 1)[0] + f".mp3"

        video_clip = VideoFileClip(mp4)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3)

        audio_clip.close()
        video_clip.close()

        os.remove(mp4)
        shutil.move(mp3, r"C:/Users/your_name/folder for music")  # Replace this with your own output directory'

    except Exception:
        if errors < 3:
            errors += 1
            print(f"Something went wrong... Trying again! {errors}")
            download_files(url)
        else:
            print("Could not download file.")


def get_mp3():
    url = input("Enter a YouTube link: ")
    start_time = time.time()

    print("Converting...")
    download_files(url)

    print(f"Time elapsed: {time.time() - start_time} seconds")


get_mp3()
