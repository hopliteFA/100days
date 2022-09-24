#####add two numbers#####
#number = input("Enter a 2 digit number: ")

#print(int(number[0]) + int(number[1]))

#####BMI calculator####
#print("BMI Calculator")
#weight = int(input("weight: "))
#height = int(input("height: "))

#bmi = (703 * weight)/height**2

#print(bmi)

####Life calculator with f strings####
age = int(input("What is your age?"))

time_left = 90 - age

years = time_left
weeks = time_left*52
days = weeks*365

print(f"You have {years} years left, which is also {weeks} weeks and {days} days left.")