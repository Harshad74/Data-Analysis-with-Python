import numpy as np 
import pandas as pd

print(pd.isna(pd.Series([1,2,3,np.nan,np.nan])))
print(pd.notnull(pd.DataFrame({'column A':[1,np.nan,7],'column B': [np.nan,2,3]})))

print(pd.Series([1,2,3,np.nan,np.nan]).count())

print(pd.Series([1, np.nan]).isnull().any())
print(pd.Series([1, 2]).isnull().any())

s = pd.Series([1, 2, 3, np.nan, np.nan, 4])

print(s.isnull().values)
print(s.isnull().values.any())