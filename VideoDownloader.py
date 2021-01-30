# It can only download the highest resolution videos from YT
from pytube import YouTube

your_link = input("Enter the link of the video")
y = YouTube(your_link)

print("Title of the video: ", y.title)
print("lenght of the video: ", y.length)
print("Video views: ", y.views)

# res = input("Choose the resolution you like!\n 0: 360p\n 1: 720p\n 2: 1080p\n")
# options = ["360", "720", "1080"]

# chosen_stream = y.streams.filter(file_extension="mp4", resolution=options[int(res)])

quality = y.streams.get_highest_resolution()
print("Downloading your video...")
quality.download()
print("Download completed!!!")