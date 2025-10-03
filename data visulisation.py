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
#pie chart
activites=["eating","sleeping","sports","crocheting","studying"]
time_spent=[2,8,1,1,3]
clrs=["red","blue","green","yellow","purple"]
plt.figure(facecolor="lightblue")
plt.pie(time_spent,labels=activites,colors=clrs,autopct='%1.0f%%',startangle=90,shadow=True)
plt.show()
#stack plot

mon=[2,8,1,2,3]
tue=[3,5,8,1,2]
wed=[3,8,7,9,1]
thu=[2,4,9,1,3]
fri=[2,4,5,2,1]
plt.stackplot(activites,mon,tue,wed,thu,fri,labels=["mon","tue","wed","thu","fri"])
plt.legend()
plt.show()
#subplots
plt.figure()
plt.subplot(2,3,4)#first num is row,second is coloumns,and third is what you want to access
plt.scatter(x,y,color="yellow",marker="^",s=30)
plt.subplot(3,3,2)
plt.pie(time_spent,labels=activites,colors=clrs,autopct='%1.0f%%',startangle=90,shadow=True)
plt.show()