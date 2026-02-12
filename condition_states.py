

'''Write a Python program that takes a character as input and checks whether it is a vowel or not. Use the if-else statement.'''


char= input("enter a character:")

if char in "aeiouAEIOU":
    print("It is vowel")
else:
    print("It is consonant")







'''Write a program that takes an age as input and classifies the person into one of the following age groups:
Child: 0-12 years
Teenager: 13-17 years
Adult: 18-64 years
Senior: 65 years and older'''


age=int(input("enter your age:"))

if age>=0 and age<=12:
    print("you are child")
elif age>=13 and age<=17:
    print("you are teenager")
elif age>=18 and age <=64:
    print("you are adult")
elif age>=65 and age<=120:
    print("you are senior citizen")
else:
    print("please enter valid age")







'''Write a program that takes an integer as input and classifies it as positive,negative, or zero. Use the if-elif-else statement.'''


number=int(input("enter number:"))

if number>0:
    print(f"{number} is postive number")

elif number<0:
    print(f"{number} is negative number")
else:
    print(f"{number} is zero")







'''Create a program that checks whether a given year is a leap year or not. A 
leap year is divisible by 4, but not by 100 unless it is divisible by 400'''


year=int(input("enter year:"))

if year%4==0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")






'''Build a simple calculator program that takes two numbers and an operator 
(+, -, *, /) as input and performs the corresponding operation'''

num_1=int(input("enter number_1:"))
num_2= int(input("enter number_2:"))
operator= input("enter operator (+,-,*,/):")

if operator=="+":
    print(f"result after addition {num_1+num_2}")
elif operator=="-":
    print(f"result after substraction {num_1-num_2}")
elif operator=="*":
    print(f"result after multiplication {num_1*num_2}")
elif operator == "/":
    print(f"result after division {num_1/num_2}")
else:
    print("please enter valid operator")






'''Rewrite the following code using the short-hand if statement:
x = 8
if x % 2 == 0: result = "Even"
else: result = "Odd"
'''

x=8
print("even") if x%2==0 else print("odd")





'''Create a program that calculates the final price after applying a discount. 
The program should take the original price and the discount percentage as input'''

ori_price=float(input('enter original price:'))
discount= float(input("enter discount in %:"))

final_price=ori_price-(ori_price*discount)/100
print(f"final price after discount {final_price}")






'''Write a program that calculates the Body Mass Index BMI using the 
formula: BMI = weight (kg) / (height (m))^2. The program should take weight and height as input'''


weight=float(input('enter your weight in kg:'))
height=float(input("enter your height in mt:"))

BMI= weight/(height)**2
print(f"your BMI is {BMI}")