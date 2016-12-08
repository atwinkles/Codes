import time

a = 1
b = 1
c = 2

i = 3

start = time.time()

while len(str(c)) < 1000:
	a = b
	b = c
	c = b + a
	i += 1

elapsed = (time.time() - start)
print "\nThe index of %d is %d. This was computed in %d seconds!\n" % (c,i,elapsed)
