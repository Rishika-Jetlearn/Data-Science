import pandas as pd
titanic_df=pd.read_csv(r"C:\Users\Manisha\Desktop\Jetlearn-python-rishika\Data-Science\titanic.csv")

#male
print(titanic_df.loc[(titanic_df["Sex"]=="male")&(titanic_df["Pclass"]==1),"Fare"])


print(titanic_df.loc[(titanic_df["Sex"]=="male")&(titanic_df["Pclass"]==2),"Fare"])

print(titanic_df.loc[(titanic_df["Sex"]=="male")&(titanic_df["Pclass"]==3),"Fare"])

#female
print(titanic_df.loc[(titanic_df["Sex"]=="female")&(titanic_df["Pclass"]==1),"Fare"])

print(titanic_df.loc[(titanic_df["Sex"]=="female")&(titanic_df["Pclass"]==2),"Fare"])

print(titanic_df.loc[(titanic_df["Sex"]=="female")&(titanic_df["Pclass"]==3),"Fare"])