import screen_ctrl.screen_size_check as screen_size_check
import os
import time

screen_lenght = screen_size_check.width_check()
screen_height = screen_size_check.height_check()

os.system('cls' if os.name == 'nt' else 'clear')

centered_screen_title_space = int((screen_lenght - 26) / 2)
def print_centered(text):
    print(' ' * centered_screen_title_space + text)
print('\n' * int((screen_height - 8) / 2))
print_centered("╔════════════════════════╗")
print_centered("║ Circuit Live Simulator ║")
print_centered("╚════════════════════════╝")
time.sleep(3)

os.system('cls' if os.name == 'nt' else 'clear')

print('Your screen size:', str(screen_lenght) + 'x' + str(screen_height), 'symbol characters')

os.system('cls' if os.name == 'nt' else 'clear')
