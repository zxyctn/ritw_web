from django.shortcuts import render
from django.http import HttpResponse

from escpos.printer import Serial

def print_text_pi(text):
    p = Serial(devfile='/dev/serial0',
            baudrate=19200,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=1.00,
            dsrdtr=True)

    p.set(align='center', font='b', width=3, height=3, custom_size=True)
    p.block_text("\n\n\n" + text + "\n\n\n", columns=12)
    p.cut()

def index(request):
    return render(request, 'pages/index.html')

def print_text(request):
    if (request.method == 'POST'):
        text = request.POST['text']
        print("WORKS")
        print(text)
        print_text_pi(text)

        return render(request, 'pages/index.html')
