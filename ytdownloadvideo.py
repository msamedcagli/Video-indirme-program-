import yt_dlp

link = input("Video linkini girin: ")

ydl_opts = {
    'outtmpl': 'indirilenler/%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

