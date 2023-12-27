# GCD recursive
GCD = lambda a,b: a if b == 0 else gcd(b,a%b)

# GCD with loops
def gcd(a,b):
    while b != 0:
        t = b
        b = a %b
        a = t
    return a