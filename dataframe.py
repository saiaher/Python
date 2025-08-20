import pandas as pd
import numpy as np
file_csv = r"C:\Sai\Github\Python\examples\test_file.csv"
s1=pd.read_csv(file_csv)
print(s1.head(3))
print(s1.shape[1])
print(len(s1.columns))
print(type( Category,axis=1))
