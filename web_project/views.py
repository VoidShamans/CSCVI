from django.shortcuts import render

def home(request):
    return render(request, 'web_project/Home.html')

def video(request):
    return render(request, 'web_project/Video.html')