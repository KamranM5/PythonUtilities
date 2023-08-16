from pytube import YouTube

link=input('Enter the link:')

url=YouTube(link)
video=url.streams.get_highest_resolution()
video.download()
print('Done!')
