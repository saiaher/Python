class number:
    def missing_number(self,list):
        n = len(list) + 1  
        for i in range(n):
            if i not in list:
                return i
        
     

s1=number()
print(s1.missing_number( [0,1, 2, 4, 5, 6,8,9,20]))  




class Number:
    def missing_number(self, lst):
    
        smallest = lst[0]
        largest = lst[0]
        for num in lst:
            if num < smallest:
                smallest = num
            if num > largest:
                largest = num

        
        missing = []
        for i in range(smallest, largest + 1):
            if i not in lst:
                missing.append(i)
        return missing

s1 = Number()
print(s1.missing_number([0, 1, 2, 4, 5, 6, 8, 9, 20]))
                       


