import numpy as np
a=[3,56,2,8,1,10]
print(a)
print(type(a))
#converting list to array
a_array=np.array(a)
print(a_array)
print(type(a_array))

#comparasion of operations
b=[]
for i in a:
    doubled=i*2
    b.append(doubled)
print(b)

#on the array
print(a_array*2)

#array of 0s
zeros=np.zeros(5,int)
print(zeros)
#2D zeros array
zeros_2d=np.zeros((2,3))
print(zeros_2d)

#ones
ones_3d=np.ones((2,3,3))
print(ones_3d)

#finding the dimentional
print(zeros.ndim)
print(zeros_2d.ndim)
print(ones_3d.ndim)

#finding the shape
print(zeros.shape)
print(zeros_2d.shape)
print(ones_3d.shape)

#size
print(zeros.size)
print(zeros_2d.size)
print(ones_3d.size)
#creating array with numbers in range
array_with_range=np.arange(3,20,2)#stop value is not included
print(array_with_range)
#mixing the items
print(np.random.permutation(array_with_range))
print(np.random.permutation(array_with_range))
print(np.random.permutation(array_with_range))
#array of random numbers
print(np.random.randint(3,20,7))
c=np.random.randint(3,20,(3,4))
print(c)
#reshaping an array
print(c.reshape(2,6))
