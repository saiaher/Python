import pandas as pd
import numpy as np
class Vowels:
    def count_vowels(self,s):
        vowels = "aeiouAEIOU"
        count=[]
        for i in s:
            if i in vowels:
                count.append(i)
        print(count )        
        return len(count )  
        
s1=Vowels()
  
print(s1.count_vowels("sai"))





# Find the Largest of Three Numbers

class Large:

    def large_number(self,s):
      
      largest=0

      for index, value in enumerate(s):
            
            if value > largest:

                largest = value

      return largest

s2=Large()

print(s2.large_number([10,20,30]))            