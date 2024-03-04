from EuclideanAlgo import gcd
# Easy method
LCM = lambda a,b: int((a*b)/gcd(a,b))

# Hard Way
# def lcm(a:int,b:int):
#     larger = a if a > b else b
#     factors = []
#     for i in range(2,larger):
#         while a % i == 0 or b % i == 0:
#             if a%i==0:
#                 a /= i
#             if b%i == 0:
#                 b /= i
#             factors.append(i)
#     lcm = 1
#     for i in factors:
#         lcm *= i
#     return lcm
