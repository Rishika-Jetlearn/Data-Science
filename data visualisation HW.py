import pandas as pd
import matplotlib.pyplot as plt
#Plot a bar graph of count of passengers in different Pclass from titanic dataset
titanic_df=pd.read_csv(r"C:\Users\Manisha\Desktop\Jetlearn-python-rishika\Data-Science\titanic.csv")
iris_df=pd.read_csv(r"C:\Users\Manisha\Desktop\Jetlearn-python-rishika\Data-Science\iris.csv")
pclass_counts = titanic_df['Pclass'].value_counts().sort_index()
plt.bar(pclass_counts.index, pclass_counts.values)

plt.title('Count of Passengers in Different Pclass (Titanic Dataset)')
plt.xlabel('Passenger Class (Pclass)')
plt.ylabel('Number of Passengers')
plt.xticks(ticks=pclass_counts.index,labels=pclass_counts.index)
plt.show() 

#Plot a histogram for age of passengers in intervals of 10 years.
plt.hist(titanic_df["Age"],10)
plt.show()

#Create scatter plot between Petal Length vs Petal Width and Sepal Length and Sepal Width
plt.scatter(iris_df["petal_length"],iris_df["petal_width"],c=pd.Categorical(iris_df["species"]).codes)#third value is to customise the colours according to the species
plt.show()
plt.scatter(iris_df["sepal_length"],iris_df["sepal_width"],c=pd.Categorical(iris_df["species"]).codes)
plt.show()