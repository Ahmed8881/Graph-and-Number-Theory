def extendedGcd(a,b):
    old_r, r = a,b
    old_s, s = 1,0
    old_t, t = 0,1
    while r != 0:
        quotient = old_r//r
        old_r,r = r,old_r-quotient*r
        old_s,s = s,old_s-quotient*s
        old_t,t = t, old_t - quotient*t
    return old_s,old_t

if __name__ == "__main__":
    s,t = extendedGcd(3,7)
    print(f"bezout coefficient are {s} and {t}")