import numpy as np
numbers=np.arange(11)
print(numbers)
answer=[]

user=int(input("1. Linear Expression\n2. Quadratic Expression\nWhich type of expression do you want to evaluate?   "))

if user==1:
    print("ax+b")
    a=int(input("Enter value for a: "))
    b=int(input("Enter value for b: "))
    linear=(a*numbers)+b
    print(linear)
elif user==2:
    print("ax^2 + bx + c")
    a=int(input("Enter value for a: "))
    b=int(input("Enter value for b: "))
    c=int(input("Enter value for c: "))
    quad=a*numbers**2 + b*numbers + c
    print(quad)