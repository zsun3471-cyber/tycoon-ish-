import os
import random
import time

def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def gambling():
    chance = random.random()
    return round(chance,2)

def typewriter(text, delay = 0.05):
    for i in text:
        print(i, end = "", flush=True)
        time.sleep(delay) 

clear_terminal()

shoplist = ["2x Luck", "Iron Pickaxe", "Golden Pickaxe", "Diamond Pickaxe", "Galvanized Square Steel Pickaxe."]
money = 0




epstienlist = ["Donald Trump", "Diddy", "Elon Musk", "Stephen Hawking"]
print(epstienlist)
epstienlist.clear()
print(epstienlist)


while True:
    typewriter("Welcome to the main menu! What would you like to do?\nYou can go mining, shopping for tools, and gamble!!!!111\n")
    mainmenu = input()
    if mainmenu.lower() == "shop" or "shop" in mainmenu.lower():
        typewriter("Welcome to the shop. You can buy stuff in here! (no way right!!??)")
        typewriter("\nYou can buy: " + ", ".join(shoplist)+ " ")
        break
    elif mainmenu.lower() == "mining" or "mining" in mainmenu.lower():
        typewriter('hi')


