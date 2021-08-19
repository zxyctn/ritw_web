from django.shortcuts import render
from django.http import HttpResponse

from . import print_text_pi

def index(request):
    return render(request, 'pages/index.html')

def print_text(request):
    if (request.method == 'POST'):
        # Get the text to be printed
        text = request.POST['text']
        # Logging received text
        print("Received:\n" + text)
        # Printing the received text
        print_text_pi(text)
        # Rendering home page again
        return render(request, 'pages/index.html')
