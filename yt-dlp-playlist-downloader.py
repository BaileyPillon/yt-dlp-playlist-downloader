from __future__ import unicode_literals
import os
import yt_dlp
import time

playlist_url = "[Insert playlist URL here]"
start_time = time.time()

def download_mp3s():
    # Create a directory to store the downloaded files
    #os.makedirs("[Insert directory here], exist_ok=True)
    
    # Set the options for yt-dlp
    ydl_opts = {
        "format": "bestaudio/bestvideo",
        "ignoreerrors": True,
        "nooverwrites": True,
        "writethumbnail": True,
        "writeinfojson": True,
        "matchtitle": #"[Name in partial or full to be matchedm, otherwise delete or comment out]",
        "outtmpl": #"[Insert directory here]/%(title)s.%(uploader)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }, {
            "key": "EmbedThumbnail",
        }]
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


def download_mp4s():
    # Create a directory to store the downloaded mp4s 
    os.makedirs("H:/Juice WRLD - Legends Never Die 3", exist_ok=True)
    
    # Set the options for yt-dlp
    ydl_opts = {
        "format_sort": ['res:bestvideo/bestaudio',"ext:mp4"],
        "ignoreerrors": True,
        "nooverwrites": True,
        "writethumbnail": True,
        "writeinfojson": True,
        "matchtitle": "Juice",
        "outtmpl": "[Insert directory here]/%(title)s.%(uploader)s.%(width)s.%(height)s.%(ext)s",
    }
            
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    download_mp4s()
    download_mp3s()
    time_taken = (time.time() - start_time) / 60
    print(f"Time taken: {time_taken:.2f} minutes")
    time_taken = time_taken / 60
    print(f"Time taken: {time_taken:.2f} hours")
