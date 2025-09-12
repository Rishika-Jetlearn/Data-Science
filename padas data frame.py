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


#reading csv file
titanic_df=pd.read_csv(r"C:\Users\Manisha\Desktop\Jetlearn-python-rishika\Data-Science\titanic.csv")
print(titanic_df)
print(titanic_df.info())

#fetch records from top,it is 5
print(titanic_df.head(3))
#fetch records from bottom
print(titanic_df.tail())

#finding shape,number of rows and coloumns
print(titanic_df.shape)

#retriving singe coloumn values(series)
print(titanic_df["Age"])
print(titanic_df["Age"].max())
print(titanic_df["Fare"].sum())

#fetching multiple coloumns
print(titanic_df[["Name","Age"]])

#filitering(selecting by condititon)
print(titanic_df[titanic_df["Age"]<18])
print(titanic_df[(titanic_df["Age"]<18)&(titanic_df["Pclass"]==1)])# or is done with |

#slicing with index
print(titanic_df.iloc[3:15:2,2:4])
print(titanic_df.iloc[[3,4,6],[2,5,6]])

#conditional slicing
print(titanic_df.loc[titanic_df["Age"]<18,["Name","Fare"]])
print(titanic_df.loc[1:5,["Name","Age"]])
#oldest person on boat
oldest=titanic_df["Age"].max()
print(titanic_df.loc[titanic_df["Age"]==oldest,["Name","Fare","Age","Survived"]])

youngest=titanic_df["Age"].min()
print(titanic_df.loc[titanic_df["Age"]==youngest,["Name","Fare","Age","Survived"]])
print("*****************************************")
#survivied
print(titanic_df.loc[titanic_df["Survived"]==1,["Name","Fare","Age"]])

print("*****************************************")
#not survivied
print(titanic_df.loc[titanic_df["Survived"]==0,["Name","Fare","Age"]])

#change values
titanic_df.loc[0:2,"Name"]=["George","John","James"]
print(titanic_df.head())
#add coloumn
titanic_df["Discount"]=titanic_df["Fare"]/2
print(titanic_df)
#rename coloumn(use inplace=true to change)
titanic_df.rename(columns={"Fare":"Price","Discount":"50% off"},inplace=True)
print(titanic_df)
#creating csv
titanic_df.to_csv("titanic_fake.csv")
#adding row
titanic_df.loc[887]=[0, 3,"Mr. Patrick Dooley","male",32.0 ,0 , 0 ,7.7500 , 3.87500]
print(titanic_df)
#sort
print(titanic_df.sort_values(by="Age"))
#replacing values
titanic_df["Sex"].replace({"female":"F","male":"M"},inplace=True)
print(titanic_df)
#aggregation function
print(titanic_df.agg({"Age":["min","max"],"Price":["sum","mean"],"Name":"count"}))
#grouping
grouped=titanic_df.groupby(by="Pclass").max()
print(grouped)
#grouping by 2 categories
print(titanic_df.groupby(by=["Pclass","Sex"]).max())
print(titanic_df.groupby(by=["Pclass","Sex"])[["Age","Price"]].mean())
#operations on text data
print(titanic_df["Name"].str.lower())
titanic_df["Last name"]=titanic_df["Name"].str.split().str.get(-1)#last item is alway index -1
print(titanic_df)