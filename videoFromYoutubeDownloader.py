from pytube import YouTube

link=input('Введи ссылку')

url=YouTube(link)
video=url.streams.get_highest_resolution()
video.download()
print('Done(готово)...')