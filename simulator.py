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

def menu_choice():
    print("What do you want to do?")
    print("╔════════════════════╗")
    print("1. Start the simulator")
    print("╚════════════════════╝")
    print("╔═══════════════╗")
    print("2. Select circuit")
    print("╚═══════════════╝")
    print("╔═════════════════════════╗")
    print("3. Add circuit to simulator")
    print("╚═════════════════════════╝")
    print("╔═════════════╗")
    print("4. Link circuit")
    print("╚═════════════╝")
    print("╔═════╗")
    print("5. Exit")
    print("╚═════╝")
    return input("Select an option: ")

choice = menu_choice()