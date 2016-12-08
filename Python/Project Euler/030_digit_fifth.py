import time

def digit_fifth(n):
    k = str(n)
    tot = 0
    for i in k:
        tot += (int(i))**5
    return tot

start = time.time()

res = []
for i in range(2,10000000):
    if i == digit_fifth(i):
        res.append(i)

total = 0
for i in res:
    total += i

elapsed = (time.time() - start)

print "\nThe sum of all numbers which are equal to the sum of the fifth power of their digits is %d. This was computed in %d seconds!\n" % (total,elapsed)
