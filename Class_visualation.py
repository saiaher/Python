import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.random import randn, randint, uniform, sample

df = pd.DataFrame (randn(1000), index = pd.date_range('2019-06-07', periods = 1000), columns=['value'])
ts = pd. Series (randn(1000), index = pd.date_range('2019-06-07', periods = 1000))
# print(ts)
# df0 = pd.DataFrame(randn(10), columns=["sai"], index=range(1,11))


# df1 = pd.DataFrame(randn(10), columns=["sai"]).cumsum()
# print(ts)

# print(df1.plot(figsize=(50,20)))
# print(plt.plot(ts))
# print(plt.show())
s1 = sns.load_dataset(('iris'))# print(s1.head())
# s1.plot()
# print(plt.show ())

# ts.plot(figsize=(1000,5))
# plt.show()

# s1.plot()
# plt.show()


# df.plot(kind='bar',figsize=(1000,5))
# plt.show()

# x=ts.plot(kind ='barh', figsize=(200,80))
# print(x)
# plt.show()

print(s1)

s2 = s1.drop(['species'], axis = 1)
print(s2.head())




