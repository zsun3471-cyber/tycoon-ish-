import os
import random

def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def gambling():
    chance = random.random()
    return round(chance,2)
clear_terminal()

money = 0

while True:
    mainmenu = input("would you like to mine for ores? Y/N")
    if mainmenu.upper() == "Y":
        chance = gambling()
        if chance >= 0.9:
            print('you found diamonds!')
            money += chance * 100000
            print(money)
        else:
            print('found nothing, aww...')
    else:
        break
