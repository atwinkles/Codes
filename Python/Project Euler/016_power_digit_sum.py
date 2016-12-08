import time

def digit_sum(a,b):
    k = a**b
    summerino = 0
    j = str(k)
    for i in j:
        summerino += int(i)
    return summerino

start = time.time()
a = 2
b = 1000
k = digit_sum(a,b)
elapsed = (time.time() - start)

print "\nThe sum of %s^%s's digits is %s, which was computed in %s seconds!\n" % (a,b,k,elapsed)
