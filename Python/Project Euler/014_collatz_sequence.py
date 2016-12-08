import time

def collatz(n):
    count = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
            count += 1
        else:
            n = 3*n + 1
            count += 1
    return count

start = time.time()
result = [13]
for a in range(1,1000000):
    if collatz(a) > collatz(result[-1]):
        result.append(a)

#print(result[-1])
#print(collatz(result[-1]))

elapsed = (time.time() - start)
print 'The result %s with a chain of length %s was computing in %s seconds' % (result[-1],collatz(result[-1]),elapsed)
