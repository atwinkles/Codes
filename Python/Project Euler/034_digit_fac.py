import time

def fac(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        tot = 1
        while n > 1:
            tot *= n
            n -= 1
        return tot

def digit_fac(n):
    k = str(n)
    tot = 0
    for i in k:
        tot += fac(int(i))

    return tot 

start = time.time()

res = []
for i in range(3,10000000):
    if i == digit_fac(i):
        res.append(i)

total = 0
for i in res:
    total += i 

elapsed = (time.time() - start)

print "\nThe sum of all numbers which are equal to the sum of the factorial of their digits is %d. This was computed in %d seconds!\n" % (total, elapsed)
