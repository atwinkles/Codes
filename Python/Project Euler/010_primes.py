primes = [2]
def prime_generator(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
       if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]] 


#print prime_generator(50)
print sum(prime_generator(2000000))

