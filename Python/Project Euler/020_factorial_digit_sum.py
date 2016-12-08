import time

def factorial(n):
    fac = n
    for i in range(1,n):
        fac *= n-i
    return fac

def factorial_digit_sum(n):
    k = factorial(n)
    j = str(k)
    count = 0
    for i in j:
        count += int(i)
    return count

start = time.time()
m = 100
result = factorial_digit_sum(m)
elapsed = (time.time() - start)

print "\nThe sum of digits of %s! is %s, which was computed in %s seconds.\n" % (m,result,elapsed)
