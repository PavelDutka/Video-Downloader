from pytube import YouTube
import os

def Download(link):
    youtubeObject = YouTube(link)
    youtubeStream = youtubeObject.streams.get_highest_resolution()
    try:
        # Set the download path to the Downloads folder
        download_path = os.path.expanduser("~/Downloads/")
        youtubeStream.download(output_path=download_path)
    except:
        print("An error has occurred")
    print("Download is completed successfully")

link = input("Enter the YouTube video URL: ")
Download(link)
