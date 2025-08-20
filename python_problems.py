import numpy as np

# fizzbuzz
s1 = []

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        s1.append("fizzbuzz")
    elif i % 5 == 0:
        s1.append("fizz")
    elif i % 3 == 0:
        s1.append("buzz")
    else:
        s1.append(str(i)) 

print(s1)

# Palindrome Checker

def palindeome(x):
    if x==x[::-1]:
        print("it's palindrome")
    else:
        print("it's not a palindrome")
palindeome("ram ram")
palindeome("121121")

# count words
 
sentence=input("enter your sentence:")

print(len(sentence.split())) 

# Find the Smallest Number

def find_smallest_number(numbers):
    if not numbers:
        return None  
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest

my_list = [1,2,3,4,5,6,0]
smallest_number = find_smallest_number(my_list)
print("The smallest number in the list is:", smallest_number)

# sum of digit:S

def sum_digit(x):
    add=0
    for i in x:
        add+=i
    return add    
        
        

s1=sum_digit([1,2,3,4,5,6])
print(s1)


# find all multiples
multiple=[]
for i in range(1,51):
    if i%3==0:
        multiple.append(i)
    elif i%5==0:
         multiple.append(i)    
print(multiple)    


