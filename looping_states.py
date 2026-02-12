
'''Write a Python program that calculates and prints the sum of the squares of 
numbers from 1 to 5 using a for loop.'''

sum=0
for i in range(1,6):
    j= i**2
    print(f"{i} square {j}")
    sum += j
print(f"sum of squares is {sum}")



'''Write a Python program that uses a while loop to print a countdown from 5 to 1'''

x=5
while x>0:
    print(x)
    x-=1




'''Write a Python program to print the multiplication table for a user-specified number using a nested for loop'''

table=int(input("enter multiplication table number:"))

for i in range(1):
    for j in range(1,11):
        print(f"{table}*{j}={table*j}")



'''Write a Python program that uses a "for" loop to find the sum of all even numbers between 0 and 10 (inclusive)'''

sum=0
for i in range(1,11):
    if i%2==0:
        sum+=i
print(f"sum of all even numbers from 0 and 10 is {sum}")





'''Calculate the sum of all numbers from 1 to a given number'''

n= int(input("enter number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(f"sum of 1 to {n} numbers is {sum}")





'''Display numbers from a list using loop'''

l=[10,2,24,67,45,62]

for i in l:
    print(i)



'''Display numbers from -10 to -1 using for loop'''

for i in range(-10,0):
    print(i)




'''Write a Python program to print the cube of all numbers from 1 to a given number'''


n= int(input("enter number:"))
sum=0
for i in range(1,n+1):
    i=i**3
    sum+=i
print(f"sum of cubes from 1 to {n} is {sum}")
    











