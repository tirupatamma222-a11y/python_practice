'''Write a Python program to calculate the area of a rectangle using the given 
formula: 
area = length * width . Take the values of length and width as inputs from 
the user'''

length=int(input("enter length of rectangle:"))
width=int(input("enter width of rectangle:"))
area=length*width
print(area)



'''Write a Python program to demonstrate incrementing and decrementing a variable'''

number_1=100
number_1 +=10    # performed incrementing a variable by 10
print(number_1)

number_2=200
number_2 -=40     # performed decrementing a variable by 40
print(number_2)




'''Write a Python program to convert temperature from Celsius to Fahrenheit. The 
formula for conversion is: 
F = (C * 9/5) + 32 . Take the temperature in Celsius as input from the user.'''

C=float(input("enter the temperature in celsius:"))
F=(C * 9/5) + 32
print(F)


'''Write a Python program to calculate the simple interest given the principal 
amount, rate, and time (in years)'''

# simple interest=PTR/100

P= int(input("enter principal amount:"))
R= float(input("enter rate of interest:"))
T= float(input("enter time in years"))
Interest = P*T*R*12/100
print(Interest)



'''Write a Python program to concatenate two strings and display the result. The 
strings should be taken as input from the user'''

first_name=input("enter first name:")
last_name=input(" enter last name:")
print(first_name+last_name)



'''Write a Python program to convert a distance from kilometers to miles'''



kilometer=float(input("enter kilometers:"))
miles=kilometer * 0.621
print(miles)

