###Even or odd###

#number = int(input("Test your number for even or odd: "))

#if number % 2 == 0:
#    print ("Your number is even!")
#else:
#    print("Your number is odd!")

###Revised BMI #####

print("BMI Calculator")
weight = int(input("weight: "))
height = int(input("height: "))

bmi = (703 * weight)/height**2

if bmi < 18.5:
    print (f"Your BMI is {bmi} and you are underweight")
elif bmi >= 18.5 and bmi < 25:
    print (f"Your BMI is {bmi} and you have normal weight")
elif bmi >= 25 and bmi < 30:
    print (f"Your BMI is {bmi} and you are slightly overweight")
elif bmi >= 30 and bmi < 35:
    print (f"Your BMI is {bmi} and you are obese")
else:
    print (f"Your BMI is {bmi} and you are clinically obese")

###Leap year calculator###

input_year = int(input("What year would you like to check?: "))
leap_or_not = ""

if input_year % 4 == 0:
      
    if input_year % 100 == 0 and input % 400 == 0:
        leap_or_not = "Leap year (100 and 400 test)"
    elif input_year % 100:
        leap_or_not = "Not a leap year (100 test)"
    
else:
    leap_or_not = "Not a leap year (4 test)"


print(leap_or_not)
            
    