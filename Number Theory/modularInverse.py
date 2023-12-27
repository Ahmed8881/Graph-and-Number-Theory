from ExtendedEuclidean import extendedGcd
from EuclideanAlgo import GCD

def inverse(a,m):
    if GCD(a,m) != 1:
        return None
    s,t = extendedGcd(a,m)
    return s if (a*s) % m == 1 else t