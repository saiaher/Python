# Problem: Count how many times each element appears in the list.


class Num:
    
    def each_num(self,list):
        count = {}
        for i in list:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        

        return count    

s1 = Num()
print(s1.each_num( [1, 2, 2, 3, 1, 4]))
        