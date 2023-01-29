from sympy import fwht 
import numpy as np

def sfwht(a):
    n = len(a)
    k = ilog2(n)
    j=1
    while j<=n:
        for i in range(0,n):
            if (i&j) == 0:
                j1=i+j 
                x=a[i]
                y=a[j1]
                a[i],a[j1]=(x+y)/2,(x-y)/2
        j*=2
    return a            

def isfwht(a):
    n = len(a)
    k = ilog2(n)
    j=1
    while j<=n:
        for i in range(0,n):
            if (i&j) == 0:
                j1=i+j 
                x=a[i]
                y=a[j1]
                a[i],a[j1]=(x+y),(x-y)
        j*=2 
    return a            

def ispow2(x):
    return not (x&x-1)

def nextpow2(x):
    x-=1
    x|=x>>1
    x|=x>>2
    x|=x>>4
    x|=x>>8
    x|=x>>16
    x|=x>>32
    x+=1
    return x 

def ilog2(x):
    return int(np.log2(x))

def grayCode(x):
    return x^(x>>1)

def grayPermutation(a):
    b = np.zeros(len(a))
    for i in range(len(a)):
        b[i] = a[grayCode(i)]
    return b

def invGrayPermutation(a):
    b = np.zeros(len(a))
    for i in range(len(a)):
        b[grayCode(i)] = a[i]
    return b

def convertToAngles(a,maxval):
    pi2=2*np.arctan(1)
    scal = pi2/maxval 
    a = a *scal 

def confertToGrayscale(a,maxval):
    pi2=2*np.arctan(1)
    scal = maxval/pi2 
    a = a * scal 


