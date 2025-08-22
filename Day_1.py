# Count Occurrences of a Character
#Takes a string s and a character c as input.Counts how many times c appears in s and prints the count.

s="sai dada" 
c="a"
appear=[]
for i in s:
    if i==c:
        appear.append(i) 

size=len(appear)
print(size)  


# Takes an integer n as input and prints the first n numbers of the Fibonacci sequence.

n = int(input(":"))
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

s1=  fibonacci(n)
print(s1)

 # Remove Duplicates from List

x=[1,1,2,2,3,3,4,4,5,5]

def remove_duplicates(input_list):
    return list(set(input_list))

# Input: list of integers
input_list = [int(x) for x in input("Enter integers separated by spaces: ").split()]

# Removing duplicates
s1 = remove_duplicates(input_list)

print(s1)





 