import pandas as pd
#converting list to series
a=[1,2,3,4,5,5,10,12,3,87]
a_series=pd.Series(a)#,index=["a","b","c","d","e"]
print(a_series)
print(type(a_series))
#operations
print(a_series.mean())
print(a_series.sum())
print(a_series.count())
print(a_series.min())
print(a_series.max())
print(a_series.median())
print(a_series.mode())
#sorting
print(a_series.sort_values())
print(a_series.sort_values(ascending=False))
#count unique values
print(a_series.value_counts())