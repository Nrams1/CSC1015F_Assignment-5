import math

f=input("Enter a function f(x):\n")

for y in range(10,-11,-1):
    for x in range(-10,11):
        if y==round(eval(f)):
            print("*",end='')
        elif y==0 and x==0:
            print("+",end='')
        elif x==0:
            print("|",end='')
        elif y==0:
            print("-",end='')
        else:
            print(" ",end='')
    print()