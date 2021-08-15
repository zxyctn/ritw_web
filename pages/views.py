from django.shortcuts import render
from django.http import HttpResponse

from src.print_text import print_text

def index(request):
    return render(request, 'pages/index.html')

def print(request):
    if (request.method == 'POST'):
        text = request.POST['text']
        
        print_text(text)
