import math

def triangle_generator(n):
    tri = n * (n+1) / 2
    return tri

def divisor_computer(n):
    divisors = [ d for d in range(2, n//2+1) if n % d == 0]
    div = [d for d in divisors if all( d % od != 0 for od in divisors if od != d) ]
    final = []
    for d in div:
        while n % d == 0:
            final.append(d)
            n = n/d 
    
    return final

def multiplicity_computer(n):
    primes = divisor_computer(n)
    exp = []
    for a in primes:
        exp.append(primes.count(a)) 
        if primes.count(a) > 1:
            primes = [value for value in primes if value != a]
    exp = [value for value in exp if value != 0]
    return exp

def factor_computer(n):
    k = triangle_generator(n) 
    kmult = multiplicity_computer(k)
    count = 1
    for l in kmult:
        count = count*(l+1)
    if count == 501:
        return k

for a in range(1,10000):
    factor_computer(a)

"""
a = 7
print(triangle_generator(a))
print(divisor_computer(triangle_generator(a)))
print(multiplicity_computer(triangle_generator(a)))
print(factor_computer(a))
"""
