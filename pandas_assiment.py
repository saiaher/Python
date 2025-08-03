import pandas as pd
import numpy as np
import math
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',

'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})
for i,j in zip(df.index,df["FlightNumber"]):
    print(i,j)
    if math.isnan(j):
                  #output 10045.0
                         #       10055.0
                         #       10065.0
                         #       10075.0

        
         df.iloc[i,1] = df.iloc[i-1,1] + 10
         print(df)

df['FlightNumber']=df['FlightNumber'].astype("int")
print(df)
print(df.columns)
#ANOTHER WAYS
# df.iloc[1,1]=10055
# df.iloc[3,1]=10075
# df['FlightNumber'] = df['FlightNumber'].astype('int')
# df['FlightNumber'] = df['FlightNumber'].astype('str')
# print(df)
df[["From","To"]]=df['From_To'].str.split("_",expand=True)
print(df)
print(type(df.iloc[1,1]))
df['From_To'] = df['From_To'].str.capitalize()

s=df[['From_To']]

s1 = df.drop(['From_To'], axis=1)
print(s1)
s2= pd.concat([df,s], axis=1)
print(s2)

s1 = pd.Series("RecentDelays")
print(s1)
df1 = pd.DataFrame(s1.tolist())
print(df)
df2 = pd.DataFrame(df['RecentDelays'].tolist(),columns=["delay1","delay2","delay3"])
print(df2)
df3=pd.concat([df,df2],axis=1)
print(df3)

















# print(df)
# df1 = df['RecentDelays'].apply(pd.Series)
# print(df1)
# s4=pd.Series("RecentDelays")
# df1 = pd.DataFrame(s4.tolist())
# print("sai")
# print(df1) 
# print(RecentDelay)





































































































