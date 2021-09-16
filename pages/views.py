from django.shortcuts import render
from django.http import HttpResponse

from .print_text_pi import print_text_pi
from .move_servo import move_servo_pi

def index(request):
    return render(request, 'pages/index.html')

def print_text(request):
    if (request.method == 'POST'):
        # Get the text to be printed
        text = request.POST['text']
        if (len(text) > 0):
            # Logging received text
            print("Received:\n" + text)
            # Printing the received text
            print_text_pi(text)
        # Rendering home page again
        return render(request, 'pages/index.html')

def move_servo(request):
    if (request.method == 'POST'):
        move_servo_pi()
        return render(request, 'pages/index.html')