from django.shortcuts import render, redirect
from django.contrib import messages

import pytube

url = ''
def Home(request):
    if request.method == "POST":
        global url
        url = request.POST['link']
        try:        
                embed_link = url.replace("watch?v=", "embed/")
                yt = pytube.YouTube(url)
                videos=yt.streams.all()
                for video in videos:
                        print(video.itag)
                return render(request, 'index.html', {'link':embed_link, 'videos':videos})
        except:
                messages.info(request,"Video not Found")
                redirect('/')

    else:
        return render(request, 'index.html')


def Download(request, id):
            try:
                yt = pytube.YouTube(url)
                videos=yt.streams.all()
                for video in videos:
                    print(video.itag)
                    if video.itag == id:
                        video.download()
                        messages.info(request,"Video Downloading")
                        return redirect('/')
            except:
                messages.info(request,"Some Problem Occurred")
                return redirect('/')