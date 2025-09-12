import pandas as pd
iris_df=pd.read_csv(r"C:\Users\Manisha\Desktop\Jetlearn-python-rishika\Data-Science\iris.csv")
#head
print(iris_df.head())
#mean
print("Mean")
print(iris_df["petal_length"].mean())
print(iris_df["petal_width"].mean())
print(iris_df["sepal_length"].mean())
print(iris_df["sepal_width"].mean())
#min
print("min")
print(iris_df["petal_length"].min())
print(iris_df["petal_width"].min())
print(iris_df["sepal_length"].min())
print(iris_df["sepal_width"].min())
#max
print("max")
print(iris_df["petal_length"].max())
print(iris_df["petal_width"].max())
print(iris_df["sepal_length"].max())
print(iris_df["sepal_width"].max())

print(iris_df[["petal_length","petal_width"]].min())
print(iris_df[["petal_length","petal_width"]].max())

#Create a dataframe with the minimum and the maximum of the petal length and the petal width
print(iris_df.agg({"petal_length":["min","max"],"petal_width":["min","max"]}))

iris_df.rename(columns={"species":"flowers"},inplace=True)
print(iris_df)
#Create a dataframe with the average sepal length and sepal width for each of the species of the flower.
print(iris_df.groupby(by="flowers")[["sepal_length","sepal_width"]].mean())
#Find the median for petal length, petal width, sepal length and sepal width for each of the species.
print(iris_df.groupby(by="flowers").median())
#Change the first species name.
iris_df.loc[0,"flowers"]="versicolor"
print(iris_df)
#Change the species names to uppercase.
iris_df=iris_df["flowers"].str.upper()
print(iris_df)