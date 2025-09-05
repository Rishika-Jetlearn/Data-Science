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

print(iris_df[["petal_length","petal_width","sepal_length","sepal_width"]].mean())