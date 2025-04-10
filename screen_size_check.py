import os
def width_check():
    size = os.get_terminal_size()
    return size.columns

def height_check():
    size = os.get_terminal_size()
    return size.lines