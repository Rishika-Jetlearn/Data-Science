import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

iris_df=iris_df=pd.read_csv(r"C:\Users\Manisha\Desktop\Jetlearn-python-rishika\Data-Science\iris.csv")

salary=pd.read_csv(r"C:\Users\Manisha\Desktop\Jetlearn-python-rishika\Data-Science\Salary.csv")
#Create a pie chart to show the distribution of each type of species from Iris dataset.
species=iris_df["species"].value_counts()
print(species)
plt.pie(species,labels=species.index,autopct="%1.0f%%")
plt.show()
#Create a subplot
plt.subplot(2,3,2)
plt.scatter(salary["YearsExperience"],salary["Salary"])

plt.subplot(2,3,4)
plt.hist(salary["YearsExperience"],5)

intevers=np.arange(1,salary["Salary"].max(),10000)
plt.subplot(2,3,6)
plt.hist(salary["Salary"],intevers)

plt.show()
