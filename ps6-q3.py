#implement the metropolis algorithm for the unit circle in q2
import random
import numpy as np

def metAlg(N,h):
    #metropolis alg for a gaussian proposal function
    sumQ=0
    for i in range(N):
        x0=random.uniform(0,1)
        y0=random.uniform(0,1)
        x1=x0+h
        y1=y0+h
        vector0=np.sqrt(x0*x0 + y0*y0)
        vector1=np.sqrt(x1*x1 + y1*y1)
        P0=np.exp(-(vector0**2)/(2))
        P1=np.exp(-(vector1**2)/(2))

        if P1>=P0:
            vector=vector1
        if P1<P0:
            if random.uniform(0,1)>=(P1/P0):
                vector=vector1
            else:
                vector=vector0
        
        if vector==vector0:
            funcVal=(x0-0.5)**2 + (y0-0.5)**2
            valQ=funcVal/P0
        
        if vector==vector1:
            funcVal=(x1-0.5)**2 + (y1-0.5)**2
            valQ=funcVal/P1
        
        sumQ+=valQ

    integral=(1/N)*sumQ
    print(integral)
    return integral

metAlg(1000,1e-3)

