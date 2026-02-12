
'''Write a Python function named add that takes two arguments a and 
b and returns their sum'''

def add(a,b):
    return a+b
sum=add(50,80)
print(sum)


'''Write a Python function named square that takes a number x as input and returns its square'''

def square(x):
   return (x**2)
print(square(7))



# Write a Python function named factorial that takes a positive integer n as input and returns its factorial.
 
def factorial(n):
    result=1 
    
    for i in range(1,n+1):
        result=result*i
    return result
    
n=int(input("enter a positive integer:"))
    
print(factorial(n))




'''Write a Python function named n as maximum that takes a list of numbers as input and 
returns the maximum value in the list'''

def maximum(numbers):
    max_val=numbers[0]
    for num in numbers:
        if num>max_val:
            max_val=num
    return max_val
n=[10,5,0,200,289,40,102,1]
print(maximum(n))




# Write a Python function named reverse that takes a string s as input and returns its reverse

def reverse(s):
    return s[::-1]

s1="renu charith"
print(reverse(s1))




'''Write a Python function named s as input and is_prime that takes a positive integer n as input 
and returns True if n is prime, otherwise False '''

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print(is_prime(8))





'''Write a Python function named fibonacci that takes a positive integer n as input and returns the
n th Fibonacci number'''

def fibonacci(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
n=8
print(fibonacci(n))





'''Write a Python function named is_palindrome that takes a string returns True if s is a palindrome, otherwise 
s as input and False '''

def is_palindrome(s):
    return s==s[::-1]
s1="2002"
print(is_palindrome(s1))






'''Write a Python function named sum_of_squares that takes a list of numbers as 
input and returns the sum of the squares of those numbers'''

def sum_of_squares(numbers):
    sum=0
    for i in numbers:
        i=i**2
        sum+=i
    return sum

n=[1,2,3,4,5]
print(sum_of_squares(n))





'''Write a Python function named average that takes a list of numbers as input and 
returns the average value'''

def average(n):
    sum=0
    for i in n:
        sum+=i
    avg=sum/len(n)
    return avg
n=[1,2,3,4,5,6,7,8]
print(average(n))


