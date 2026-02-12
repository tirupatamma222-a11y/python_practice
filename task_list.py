
'''Write Python code to reverse the order of elements in the given list Print the reversed list.
my_list = [10, 20, 30, 40, 50, 11]'''

my_list=[10,20,30,40,50,11]
#print(my_list[::-1])
my_list.reverse()
print(my_list)




'''Given two lists list1 and list2 , find and print the common elements between 
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]'''

my_list=[]
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]

for i in list1:
    for j in list2:
        if i==j:
            my_list.append(i)
print(my_list)




'''Create a new list unique_list containing only the unique elements from the 
given list original_list . Print the unique list.
original_list = [1, 2, 2, 3, 4, 4, 5]'''

original_list=[1,2,6,3,2,4,4,3,5]
unique_list=[]

for i in original_list:
    if i not in unique_list:
        unique_list.append(i)
    
print(unique_list)





'''Remove duplicate elements from the given list without duplicates while preserving the order.duplicated_list and print the list 
duplicated_list = [1, 2, 2, 3, 4, 4, 5]'''

duplicate_list=[1,2,6,3,2,4,4,3,5]
duplicated_list=[]

for i in duplicate_list:
    if i not in duplicated_list:
        duplicated_list.append(i)
    
print(duplicated_list)





'''Write a Python script that concatenates two lists and prints the result'''

list_1=[1,3,5,8,9]
list_2=[4,6,5,3,8]
list_1.extend(list_2)
print(list_1)




'''Write a Python script that repeats a list three times and prints the result'''

list_1=[1,2,3,4,5]
for i in range(1,4):
    print(list_1)




'''Write a Python script that removes the elements at even indices from a list'''

list_1=[1,2,3,8,7,9,4]
result=list_1[1::2]
print(result)





'''Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list'''

list_1=[5,9,8,7,6,1]

list_1.insert(0,10)
list_1.insert(0,11)
list_1.insert(0,12)
print(list_1)





'''Square Numbers: Create a list of squares of numbers from 1 to 10'''

list=[]

for i in range(1,11):
    i=i**2
    list.append(i)
print(list)





''' Even Numbers: Generate a list of even numbers from 1 to 20.'''

list=[]

for i in range(1,21):
    if i%2==0:
        list.append(i)
print(list)





'''Words Lengths: Given a list of words, create a list containing the lengths of each word
words = ["apple", "banana", "cherry", "date"]'''

words=["apple","banana","cherry","date"]
list=[]
for i in words:
    i=len(i)
    list.append(i)
print(list)



















