from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'entrance/index.html')

def about(request):
    return render(request, 'entrance/about.html')

def favs(request):
    return render(request, 'entrance/favs.html')

def entr(request):
    return render(request, 'entrance/entr.html')

def nature(request):
    return render(request, 'entrance/nature.html')