import random

# ###Flip a coin and return it###

# flip = random.randint(1,2)
# print(flip)

# if flip == 1:
#     print("heads!")
# else:
#     print("tails")

# ###Credit Card Roulette###

# #get names
# names_string = input("Enter names separated by a comma: ")
# names = names_string.split(", ")

# print(len(names))

# #pick name
# #-1 b/c shift left since starting at 0
# print(names[random.randint(0, len(names)-1)]) 

###Treasure Map###
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]

# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# column = int(position[0])
# row = int(position[1])

# print(column, row)

# map[row - 1][column - 1] = "X"

# print(f"{row1}\n{row2}\n{row3}")

###Rock, paper, scissors

rsp = ["rock", "paper", "scissors"]

human_number = input("Pick R/S/P with 0 (rock), 1 (paper), 2 (scissors): ")

human_choice = rsp[int(human_number)]
cpu_choice = rsp[random.randint(0,2)]

print(f"You picked {human_choice}!")
print(f"The computer picked {cpu_choice}!")

if human_choice == "rock":
    if cpu_choice == "paper":
        print("You lose!")
    elif cpu_choice == "rock":
        print("A tie!")
    else:
        print("You won!")

if human_choice == "paper":
    if cpu_choice == "scissors":
        print("You lose!")
    elif cpu_choice == "paper":
        print("A tie!")    
    else:
        print("You won!")

if human_choice == "scissors":
    if cpu_choice == "rock":
        print("You lose!")
    elif cpu_choice == "rock":
        print("A tie!")
    else:
        print("You won!")


