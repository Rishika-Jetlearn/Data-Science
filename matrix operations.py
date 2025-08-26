import numpy as np
#Make a choice-based program where you can add and subtract two matrices(2D arrays) by taking matrices and operations as user input.
rows=int(input("How many rows would you like?"))
col=int(input("How many columns would you like?"))
a=[]
for i in range(rows*col):
    numbers=int(input("Enter the value: "))
    a.append(numbers)
array1=np.array(a)
array1=array1.reshape(rows,col)
print(array1)

b=[]
for i in range(rows*col):
    n=int(input("Enter the value: "))
    b.append(n)
array2=np.array(b)
array2=array2.reshape(rows,col)
print(array2)

print(array1+array2)
print(array1-array2)