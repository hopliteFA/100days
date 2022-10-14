# ###Calculate the average height using a for loop###

# #get inputs and convert to a list
# heights = input("Give me your heights separated by a space: ")
# height_list = heights.split(" ")

# #calculate and print the average
# total = 0
# count = 0

# for height in height_list:
#     total += int(height)
#     count += 1

# average_height = total / count

# print(f"The average height is: {average_height}.")

###High score calculator###

# scores = input("Enter your scores separated by spaces: ")

# score_list = scores.split(" ")
# print(score_list)
# high_score = 0 
# for score in score_list:
#     if int(score) > high_score:
#         high_score = int(score)

# print(high_score)

# ### calculate the sum of even numbers for 1 to 100
# total = 0
# for number in range(0,101,2):
#     total += number

# print(total)

# ##FizzBuzz###

# #if div 3, Fizz.  If div 5, buzz.  If 3 and 5, fizzbuzz

# for number in range(1, 100):
#     if number % 3 == 0 and number % 5 == 0:
#         print("fizzbuzz")
#     elif number % 5 == 0:
#         print("buzz")
#     elif number % 3 == 0:
#         print("buzz")
#     else:
#         print(number)

###Password Generator###

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []

num_of_letters = input("How many letters would you like?")
num_of_numbers = input("How many numbers would you like?")
number_of_symbols = input("How many symbols would you like?")

for letter in range(0, int(num_of_letters)):
    password.append(letters[random.randint(0,25)])

for number in range(0, int(num_of_numbers)):
    password.append(numbers[random.randint(0,9)])

for number in range(0, int(number_of_symbols)):
    password.append(symbols[random.randint(0,8)])

print(f"Unshuffled password: {password}")

random.shuffle(password)

#forgot how to make a list a sting - join it!
print(f"Your shuffled password: {''.join(password)}")