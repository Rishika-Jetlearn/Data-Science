import numpy as np
import matplotlib.pyplot as plt
x=np.arange(11)

answer=[]

user=int(input("1. Linear Expression\n2. Quadratic Expression\nWhich type of expression do you want to evaluate?   "))

if user==1:
    print("ax+b")
    a=int(input("Enter value for a: "))
    b=int(input("Enter value for b: "))
    linear=(a*x)+b
    plt.plot(x,linear)
    plt.title(f"{a}x+{b}")
elif user==2:
    print("ax^2 + bx + c")
    a=int(input("Enter value for a: "))
    b=int(input("Enter value for b: "))
    c=int(input("Enter value for c: "))
    quad=a*x**2 + b*x + c
    plt.figure(figsize=(8,6))
    plt.plot(x,quad)

plt.show()