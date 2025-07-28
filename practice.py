import numpy as np
import pandas as pd
data = [{"a": 1, "b": 2, "c": 3},
 {"a": 4, "b": 5, "c": 6},
 {"a": 7, "b": 8, "c": 9}]
# s1=pd.Dataframe 
s1=pd.DataFrame(data)
s1["d"]=s1["a"]+s1["b"]
print(s1)
print(type(s1.describe()))