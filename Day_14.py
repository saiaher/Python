class String:
    def longest_substring(self, s):
       
        longest = ""
        
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
               
                if substring == substring[::-1]:
                    
                    if len(substring) > len(longest):
                        longest = substring
        
        return longest
           

s1 = String()
print(s1.longest_substring("forgeeksskeegfor"))