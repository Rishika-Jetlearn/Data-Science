import matplotlib.pyplot as plt
import numpy as np

x=np.arange(2,11,2)
y=[3,8,6,4,1]
#line plot
#if you want a figure
plt.figure(figsize=(8,6))
plt.plot(x,y,"m:D",label="line",linewidth=4)
#title
plt.title("Line plot")
#labels
plt.xlabel("Hours spent revising")
plt.ylabel("Test Scores")
#masking values
plt.xticks(ticks=x,labels=["A","B","C","D","E"],rotation=90)
#appearing the label
plt.legend()
plt.show()



#new plot
x=np.arange(1,11,0.5)#arange (the steps) can change the gap between the lines and linspace can add more numbers
y=x**2
plt.plot(x,y,"m--v",label="y=x^2")
plt.plot(x,x**3,label="y=x^3")
plt.legend()
plt.show()


#bar plot
plt.bar([1,3,5,7,9],[30,4,16,20,44])
#multiple bar plots
plt.bar([2,4,6,8],[12,67,90,32],color="orange")

plt.show()

#bar plot with categorical data
plt.bar(["female","male"],[10,5],0.4)
plt.show()

#histogram
ages=np.random.randint(10,80,30)
print(ages)
intervals=np.arange(10,81,10)
plt.hist(ages,intervals)
plt.show()
#scatter plot
x=np.arange(2,12,3)
y=[8,9,6,3]
plt.scatter(x,y,color="yellow",marker="^",s=30)
plt.show()