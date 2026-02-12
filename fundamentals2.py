# fundamentals task-2


'''Define a list containing three different data types.
Define a set containing employee idʼs'''


# list is a mutable datatype 
# below list is defined containing different datatypes

sample_data=[3,67,6.8,2.9,"python",(3,6.7),{4,6,2}]    # declaration of list containing different datatypes
print(sample_data)   
sample_data2={34,35,37,60,63} # declaration of set containing unique elements
print(sample_data2)



'''Concatenate two strings and print the result.
Repeat a string three times and display the output'''

sample_data3="this is my name"
sample_data4=" tirupathamma"
sample_data5=" and i am 30years old"
result_5=print(sample_data3+sample_data4+sample_data5)

#  in the above code performed string concatenation using three strings




'''Create a variable with a name that is a Python keyword. What happens? 
observation'''

class_1=20   # error is showing when we declared a variable with the name of keyword
print(class_1)




'''Take the user's age as input and print a message using that input'''

age=input("enter employee age:")   # input function is used to take the value by user
print(age)                          # displayed the age using print statement




'''Implement a program that uses a dictionary to store information 
about a book (title, author, publication year)'''

sample_data6={"title":"powerful thoughts","author":"cv narayana","publication year":1992}   # declared dictionary datatype
print(sample_data6)



'''Write a python program that takes a string as input 35 and return 
float value'''


data_3="3556"          # declaration of a string
data_4=float(data_3)    # converted integer to float by using float class
print(data_4)
print(type(data_4))



'''Write a program to take two names as input and print them together'''

data_5=input("enter first name:")
data_6=input("enter last name:")
print(data_5+data_6)  # performed string concatenation by taking two names as input



'''Create a program that takes user input for their age, converts it to 
an integer, adds 5, and then prints the result'''


data_7=int(input("enter age:"))
data_8=data_7+5
print(data_8)



'''Build a calculator program that takes two numbers as input and 
performs the arithmetic operation'''

number_1=int(input("enter number1:"))
number_2=int(input("enter number2:"))
result_6=print(number_1+number_2)







