from escpos.printer import Serial

def print_text_pi(text: str):
    # Establishing connection
    p = Serial(devfile='/dev/serial0',
            baudrate=19200,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=1.00,
            dsrdtr=True)

    # Printing configuration
    p.set(align='center', font='b', width=2, height=2)
    p.text("\n\n\n\n" + text + "\n\n\n\n")
    p.cut()