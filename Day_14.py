# Given a string s, find the longest substring of s that is a palindrome.
# string :- forgeeksskeegfor

class string:
    
    def longest_substring(self,str):
        for i in str:
            if str[i]==str[i+1][::-1]:
                return i
s1=string()
print(s1.longest_substring("forgeeksskeegfor"))            

                