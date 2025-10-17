import pandas as pd
data_df=pd.read_csv(r"C:\Users\Manisha\Desktop\Jetlearn-python-rishika\Data-Science\Data.csv")
print(data_df.isnull().sum())#if there are missing values
#how to treate missing values
#1. Remove the records with missing values
"""data_df.dropna(inplace=True)
print(data_df.isnull().sum())
print(data_df)"""
#2.Try and replace the values
