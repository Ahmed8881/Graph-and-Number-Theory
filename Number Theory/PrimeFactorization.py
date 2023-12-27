from math import sqrt

def primeFactors(n):
    factors = []
    while n%2==0:
        factors.append(2)
        n/=2
    for i in range(3,int(sqrt(n))+1,2):
        while n % i == 0:
            factors.append(i)
            n /= i
    if n>2:
        factors.append(n)
    return list(set([int(i) for i in factors]))
if __name__ == "__main__":
    number = input("Enter a number to factorize: ")
    while not number.isdecimal():
        print("Invalid Input\nTry Again")
        number = input("Enter a number to factorize: ")
    print(primeFactors(int(number)))