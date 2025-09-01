# Write a Python function that merges two sorted lists into a single sorted list.
import pandas as pd
import numpy as np

class Sort:
    def murge_sorted_list(self,list1,list2):
        murge_list=[]
        list=list1+list2
        for i in list:
            murge_list.append(i)
            

        murge_list.sort()

        return murge_list
    

s1=Sort()
print(s1.murge_sorted_list([1, 3, 5], [2, 4, 6]))