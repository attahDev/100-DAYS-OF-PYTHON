print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

path1 = input('''You walk down the path and reach the end of the road.
The road splits into two paths, which path do you take. (Left or Right) ''').lower()

if path1 == "left":
    path2 = input('''You go down left and enter the whispering forest. the trees beckons to you to, promising safety under their branches.
     Do you rest (Y/N)''').lower()

    if path2 == "n":
        path3= input('''You walk down the path and reach the end of the forest. In-front of you lies a river.
         Do you swim across or wait till tomorrow for a boat. (swim/wait)''').lower()
        if path3 == "wait":
            path4 = input('''You wait for the boat and finally get into the temple. in front of you lies 3 doors. Black, White, Red.
            Which do you choose? (white/black/red)''').lower()
            if path4 == "black":
                print("Congratulations, you win!")
            elif path4 == "white":
                print("You got eaten by the monster")
            elif path4 == "red":
                print("You fell into a pit of spikes")
            else:
                print("Wrong Input. You lose")

        elif path3 == "swim":
            print("You got eaten by crocodiles.")
        else:
            print("Wrong Input. You lose")

    elif path2 == "Y":
        print("The tress kill you in your sleep")

    else:
        print("Wrong Input. You lose")

elif path1 == "right":
    print("You walk down the path and reach the end of the road. No treasure island.")

else:
    print("Wrong Input. You lose")
