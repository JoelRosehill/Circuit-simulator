import screen_size_check
import os

screen_lenght = screen_size_check.width_check()
screen_height = screen_size_check.height_check()

os.system('cls' if os.name == 'nt' else 'clear')

print("╔════════════════════════╗")
print("║ Circuit Live Simulator ║")
print("╚════════════════════════╝")

print('Your screen size:', str(screen_lenght) + 'x' + str(screen_height), 'symbol characters')