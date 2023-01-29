from helper_funcs import *
from qiskit import QuantumCircuit

def cFRQI(a,compression):
    a = convertToAngles(a,1) # convert grayscale to angles
    
    n = len(a)
    k = ilog2(n)
    
    a = 2*a 
    a = sfwht(a)
    a = grayPermutation(a) 
    
    idx = list(range(0,n))


#set smallest absolute values of a to zero according to compression param
    cutoff = (compression/100.0) * n
    for it in idx[:cutoff]:
        a[it]=0.0
    


    