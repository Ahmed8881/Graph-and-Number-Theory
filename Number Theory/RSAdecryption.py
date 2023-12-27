from PrimeFactorization import primeFactors
from EuclideanAlgo import GCD
from modularInverse import inverse

def RSAdecrypt(encryptionKey:tuple):
    n,e = encryptionKey
    p,q = primeFactors(n)
    n1 = (p-1)*(q-1)
    if GCD(e,n1) != 1:
        return None
    d = inverse(e,n1)
    return d
    
print(RSAdecrypt(2537,13))