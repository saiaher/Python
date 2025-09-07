# Longest Substring Without Repeating Characters
# Find length of the longest substring with all unique characters.



class List:
    
    def Unique_list(self,string):

        substring = []
        for i in string:

            if i not in substring:
                substring.append(i)
                print(substring)
        return len(substring)      

s1= List()

count=s1.Unique_list("saimachindraaher")
print(count)







