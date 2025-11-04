import os
import random

def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
clear_terminal()


money = 0
chance = None
