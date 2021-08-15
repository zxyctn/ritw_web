from django.shortcuts import render
from django.http import HttpResponse

from escpos.printer import Serial

def print_text(text):
    p = Serial(devfile='/dev/serial0',
            baudrate=19200,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=1.00,
            dsrdtr=True)

    p.set(align='center', font='b', width=2, height=2)
    p.text("\n\n\n\n" + text + "\n\n\n\n")
    p.cut()

def index(request):
    return render(request, 'pages/index.html')

def print(request):
    if (request.method == 'POST'):
        text = request.POST['text']
        print("WORKS")
        print(text)
        print_text(text)
