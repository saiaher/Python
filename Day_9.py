# Write a Python function that counts the number of times each element appears in a list and returns a dictionary with the counts.

def count_occurrences(lst):
    counts = {} 
    it = iter(lst)  
    try:
        while True: 
            item = next(it)  
            if item in counts: 
                counts[item] += 1
            else:
                counts[item] = 1  
    except StopIteration:
        pass  
    
    return counts  

example_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result = count_occurrences(example_list)
print(result)
