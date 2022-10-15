#Hangman Challenge

import random
import os

def get_guess():
    guess = input("\nWhat is your letter guess?:  ")
    return guess

def check_guess(guess):
    counter = 0
    global misses #must declare as global to change from a function

    print(f"\nYou guessed the letter {guess}:\n")
    if guess in secret_word:
        for letter in secret_word:
            if letter == guess:
                print("\nHIT")
                current_guessed[counter] = guess
            counter +=1 
    else:
        misses -= 1

    return current_guessed

##################
#### SETUP ####
##################

#set guess to enter the while loop and the guessed letters
guess = 'y'
guessed_letters = []
misses = 10

#generate a random word
word_list = ['potato', 'sword', 'generator']
secret_word = random.choice(word_list)

#count the letters and present the blanks
current_guessed = []

for letter in secret_word:
    current_guessed.append("_")
os.system('cls')
print("\nWelcome to Hangman! Enter 'q' to quit. \n\nYour word is: \n")
print(" ".join(current_guessed))

#########################
#### RUN THE GAME ####
#########################

while guess != 'q':
    guess = get_guess()
    current_guessed = check_guess(guess)
    print(current_guessed)
    guessed_letters.append(guess)
    print(f"\nYour guessed letters {guessed_letters}")
    print(f"\nMisses remaining: {misses}")

    if "".join(current_guessed) == secret_word:
        print("\n\nYOU WON!!!\n\n")
        break
    
    if misses == 0:
        print("Game Over!  Better luck next time.")


