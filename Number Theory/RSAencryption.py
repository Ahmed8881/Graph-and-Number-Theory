from PrimeFactorization import primeFactors
from EuclideanAlgo import GCD

alphabets = 'abcdefghijklmnopqrstuvwxyz'

# To convert alphabets to digits
def toDigits(message:str):
    numeric = ''
    for i in message.lower():
        if not i.isspace():
            index = str(alphabets.find(i))
            if len(index) == 1:
                index = '0' + index
            numeric += index
    return numeric

# To get 4 digit blocks
sliceString = lambda string,blockSize: [int(string[i:i+blockSize]) for i in range(0,len(string),blockSize)]

# To covert digits to alphabets
def toAlpha(digits:list[int]):
    digits = [str(i) for i in digits]
    digits = ['0' + i for i in digits if len(i) < 4]
    digits = ''.join(digits)
    digits = sliceString(digits,2)
    digits = [i % 26 for i in digits]
    return ''.join([alphabets[i] for i in digits])

# RSA Encryption
def RSAencrypt(key:tuple,message:str):
    n,e = key
    p,q = primeFactors(n)
    if GCD(e,(p-1)*(q-1)) != 1:
        return None
    message = sliceString(toDigits(message),4)
    cipher = []
    for i in message:
        cipher.append((i**e) % n)
    return toAlpha(cipher)

if __name__ == "__main__":

    message = input("Enter message to encrypt: ")  
    while not message.isalpha():
        print("Invalid input\nTry Again")
        message = input("Enter message to encrypt: ")  

    print(RSAencrypt((2537,13),message))