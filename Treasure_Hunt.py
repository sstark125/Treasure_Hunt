import os
def ConsoleClear():
    os.system('cls' if os.name == 'nt' else 'clear')


ConsoleClear()
print('''          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/''')

print("Welcome to Treasure Island\nYour mission is to find the treasure.\n")

userChoice = (input("You're at a cross road. Where do you want to go? Type \"Left\" or \"Right\"\n")).upper()

if userChoice == "LEFT":
    ConsoleClear()
    userChoice = (input("You came to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n")).upper()
    if userChoice == "WAIT":
        ConsoleClear()
        userChoice = (input("You make it to the island. There is a house with 3 doors. Which door do you enter: Blue, Red, or Yellow?\n")).upper()
        if userChoice == "YELLOW":
            ConsoleClear()
            print("You Win!")
        else:
            ConsoleClear()
            print("Game Over")
    else:
        ConsoleClear()
        print("Game Over")
else:
    ConsoleClear()
    print("Game Over")