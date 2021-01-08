
import numpy as np 

def ranNum(a,b,x0):
    vals=[]
    vals.append(x0)
    for i in range(20):
        x1=(a*x0)%b
        vals.append(x1)
        x0=x1
    print(vals)
    return vals

ranNum(7,11,3)
print("effect of changing x0")
ranNum(7,11,20)
print("effect of changing a")
ranNum(20,11,3)