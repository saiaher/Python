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
