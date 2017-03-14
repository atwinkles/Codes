import time

start = time.time()

champernowne = ""

count = 0

while count < 1000000:
    count += 1
    champernowne += str(count)

#print champernowne
print (int(champernowne[0])* int(champernowne[9])* int(champernowne[10**2-1]) * int(champernowne[10**3-1]) * int(champernowne[10**4-1]) * int(champernowne[10**5-1]) * int(champernowne[10**6-1]))
#print champernowne[10]

elapsed = (time.time() - start)*1000
print "This was computed in %d miliseconds" % (elapsed)
