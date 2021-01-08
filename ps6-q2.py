#use monte carlo integration to find the area of a unit circle and use a unit square as the bounding volume
import random
import numpy as np
import matplotlib.pyplot as plt

def mcInt(V,N):
    sumFunc=0
    funcVal=[]
    for i in range(N):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        area=(x-0.5)**2 + (y-0.5)**2
        if area<(0.5**2):
            sumFunc+=1
            funcVal.append(1)
        else:
            funcVal.append(0)

    #calculating the error
    avFunc=(1/N)*sumFunc
    sumError=0
    for i in range(N):
        sumError+=(funcVal[i]-avFunc)**2
    sigmaF=np.sqrt((1/(N-1))*sumError)
    error=(V/np.sqrt(N))*sigmaF
        
    area=(V/N)*sumFunc
    print(area,error)
    return(area,error)

mcInt(1,1000)
print(np.pi/4)

Nvals=np.arange(100,1000,20)
print(Nvals)

error=[]
for i in range(len(Nvals)):
    error.append(mcInt(1,Nvals[i])[1])

plt.plot(Nvals,error)
plt.show()

        
