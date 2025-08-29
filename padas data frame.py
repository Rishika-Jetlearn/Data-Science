import pandas as pd
#creating data frame from dictionary
data={"name":["john","mark","priya","janvi"],"age":[15,15,16,17],"score":[22,33,51,12]}
data_in_frame=pd.DataFrame(data,index=["s1","s2","s3","s4"])
print(data_in_frame)
print(type(data_in_frame))

#data frame using list
d=[["john",15,22],["mark",15,33],["priya",16,51],["janvi",17,12]]
d_dataframe=pd.DataFrame(d,columns=["name","age","score"])
print(d_dataframe)
print(d_dataframe.index)
print(d_dataframe.columns)
print(data_in_frame.index)
#fetch complete info
d_dataframe.info()
#descriptive statistics
print(d_dataframe.describe())