import matplotlib.pyplot as plt
import numpy as np

x=np.arange(2,11,2)
y=[3,8,6,4,1]
#line plot
#if you want a figure
plt.figure(figsize=(8,6))
plt.plot(x,y,"m:D")
#title
plt.title("Line plot")
#labels
plt.xlabel("Hours spent revising")
plt.ylabel("Test Scores")
#masking values
plt.xticks(ticks=x,labels=["A","B","C","D","E"])

plt.show()
