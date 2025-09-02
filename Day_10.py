#  Implement a Stack Using Lists

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = []

for i in list1:
    if i in list2:
        common_elements.append(i)


print("Common elements:", common_elements)


# Find the Kth Largest Element in an Array
 

def find_kth_largest(arr, k):
    
    arr.sort(reverse=True)
    
   
    return arr[k-1]

arr = [12, 3, 5, 7, 19, 10]
k = 3

result = find_kth_largest(arr, k)
print(f"The {k}th largest element is: {result}")
