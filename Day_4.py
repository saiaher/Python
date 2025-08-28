# Count Pairs with a Given Sum

class sum:
    def count_pair(self,number, target):

        for i in number:
            two_add=number[i]+number[i+1]
            if two_add==target:
                return [i,i+1]
        
sai=sum()
print(sai.count_pair([1,2,3,4],7))




# Check if a String is a Palindrome

class palindrome:
    #input=input("enter your string:")
    def palindrome_cheker(self,input):
        if input[::-1]==input:
            return True
        else:
            return False

s2=palindrome() 
print(s2.palindrome_cheker("racecar"))  







