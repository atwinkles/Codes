import time

def self_power(n):
    return n**n

def series(n):
    result = 0
    for i in range(1, n+1):
        result += self_power(i)
    return result

start = time.time()
final = series(1000)
sfinal = str(final)[len(str(final))-10:]
elapsed = (time.time() - start)

print "The result, %s, was computed in %d miliseconds" % (sfinal, elapsed*1000)

