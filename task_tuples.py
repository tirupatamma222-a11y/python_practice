

'''Create a Tuple Write a program that creates a tuple containing three 
elements: your name, your age, and your favorite color. Then print the tuple'''


my_deatils=("Renu",30,"blue")
print(my_deatils)




'''Access Tuple Elements Write a program that creates a tuple containing the 
days of the week. Then, print the third element of the tuple'''

week=("sun","mon","tue","wed","thu","fri","sat")
print(week[2])




'''Tuple Concatenation Write a program that creates two tuples, one 
containing odd numbers from 1 to 5 and another containing even numbers 
from 2 to 6. Concatenate these two tuples and print the result'''

t1=(1,3,5)
t2=(2,4,6)
print(t1+t2)




'''Tuple Unpacking Write a program that defines a tuple containing the 
dimensions of a rectangle (length and width). Then, unpack this tuple into 
two variables and calculate the area of the rectangle'''

dimensions=(25,30)
length=dimensions[0]
width=dimensions[1]
area=length*width
print(f"area={area}")



'''Check if an Element Exists Write a program that checks if a given element exists in a tuple'''

t=(2,5,6,1,3,7)
print(1 in t)


'''Write a Python program to generate a bill for a supermarket purchase. The 
program should store the items and their prices in a list of tuples. It should 
then iterate over this list to print out each item along with its price. Finally, 
calculate and print the total cost of all the items
Sample Input:
items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]'''


items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]


print("item\t\tprice")
print("-"*25)
total=0
for i,j in items:
    print(f"{i}\t\t{float(j)}")
    total+=j
print("-"*25)
print(f"total\t\t{float(total)}")
