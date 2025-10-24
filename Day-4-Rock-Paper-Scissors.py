import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

my_list = [rock, paper, scissors]

choices = int(input("What do you choose? pick 0 for rock, 1 for paper, 2 for scissors: "))
rand = random.choice(my_list)

if choices == 0:
    if rand == rock:
        print(my_list[0])
        print("You Tie!")
    elif rand == paper:
        print(my_list[1])
        print("You lose!")
    else:
        print(my_list[2])
        print("You win!")

elif choices == 1:
    if rand == rock:
        print(my_list[0])
        print("You win!")
    elif rand == paper:
        print(my_list[1])
        print("You tie!")
    else:
        print(my_list[2])
        print("You lose!")
elif choices == 2:
    if rand == rock:
        print(my_list[0])
        print("You lose!")
    elif rand == paper:
        print(my_list[1])
        print("You win!")
    else:
        print(my_list[2])
        print("You tie!")

else:
    print("Wrong Input")
