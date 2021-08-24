import textwrap

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

    # Flipping and re-ordering the text fragments
    text_list = textwrap.wrap(text, width=12,  initial_indent="", subsequent_indent="",
                              expand_tabs=True, replace_whitespace=True,
                              fix_sentence_endings=False, break_long_words=True,
                              drop_whitespace=True, break_on_hyphens=True, tabsize=8,
                              max_lines=None)

    # Reversing the list to print fragments in the correct order
    text_list.reverse()

    # Debug code
    print(text_list)

    # Printing configuration
    p.set(align='center', font='b', width=3,
          flip=True, height=3, custom_size=True)

    for t in text_list:
        p.block_text(t, columns=12)
    p.cut()
