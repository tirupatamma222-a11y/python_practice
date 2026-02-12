
'''Write a Python function 
square_all(numbers) that takes a list of numbers as input 
and returns a new list containing the square of each number in the input list. 
Use the 
map() function with a lambda function to implement this'''


def square_all(numbers):
     return list(map(lambda x:x**2,numbers))
numbers=[2,3,4,5,6,7]
result=square_all(numbers)
print(result)
    

'''Write a Python function 
filter_positive(numbers) that takes a list of numbers as 
input and returns a new list containing only the positive numbers from the 
input list. Use the 
filter() function with a lambda function to implement this'''

def filter_positive(numbers):
     return list(filter(lambda x:x>0, numbers))
numbers=[-4,0,-2,3,78,32,-89]
result=filter_positive([-4,0,-2,3,78,32,-89])
print(result)


'''Write a Python function 
calculate_factorial(n) that calculates the factorial of a 
given number n. Use the 
reduce() function with an appropriate lambda 
function to implement this'''

from functools import reduce

def calculate_factorial(n):
     return reduce(lambda a,b:a*b, range(1,n+1))

n=int(input("enter number:"))
result=calculate_factorial(n)
print(result)



'''Write a Python function 
count_vowels(string) that takes a string as input and 
returns the count of vowels (a, e, i, o, u) in the input string. Use the 
reduce() 
function with an appropriate lambda function to implement this'''


def count_vowels(string):
    return reduce(lambda a,b:a+(b.lower()in 'aeiouAEIOU'),string,0)

string=input("enter string:")
result=count_vowels(string)
print(result)




