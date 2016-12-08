import math,time

def lattice_routes(m,n):
    k = math.factorial(m + n)/(math.factorial(n)*math.factorial(m))
    return k

start = time.time()
m = 20
n = 20
final = lattice_routes(m,n)
elapsed = (time.time() - start)

print "The solution to the number of lattices paths for a %s x %s grid is %s and was computed in %s seconds" % (m,n,final,elapsed)
