import pandas as pd
import numpy as np
s1=pd.read_csv(r"C:\Sai\Github\Python\examples\test_file.csv")
# print(s1)
# print(s1.drop(0))
# print(s1.drop("e",axis=1))
# print(s1.rename(columns={"e":"sai"}))
# print(s1["a"][0])
# print(len(s1))
# s1["ram"]=[6 for i in range(len(s1))]
# print(s1)


s2=pd.read_csv(r"C:\Sai\Github\Python\examples\test_file.csv")
# print(s2)
# print(pd.concat([s1,s2]))
# print(pd.merge(s1,s2))

# print(s1.dtypes)
# print(s2)

# s3=pd.Series([type,sum,max])
# print(s3)
# s2["new_col"]=s2["a"]+s2["b"]
# print(s2)
# #print(s2)
# print(s1>0)
# print(s1>1)
# print(s2[s1>0])
# print(s1[s1>0])
# print(s1['a']>s2['b'])
# print(s2[s1["d"]>3])
# print(s2.reset_index())
print(s2.reset_index())
print(s2.reset_index(drop=True))
print(s2.set_index("a"))
s4=pd.MultiIndex.from_tuples(s2)
print(s4)
s5=pd.DataFrame(data=np.round(s2),index=s4)
print(s5)
print(s5.loc["a"])
print(s5.dropna())
print(s5.dropna(axis=0,thresh=1))
print(s5)

print(s5.fillna(2))
print(list(s5.groupby("a")))
