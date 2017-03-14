import time

def tri(n):
    return n*(n+1)/2

def pent(n):
    return n*(3*n-1)/2

def hexi(n):
    return n*(2*n-1)

trivalues = []
pentvalues = []
hexvalues = []

for i in range(286,10000):
    trivalues.append(tri(i))

for i in range(166,10000):
    pentvalues.append(pent(i))

for i in range(144,10000):
    hexvalues.append(hexi(i))

for i in hexvalues:
    for j in pentvalues:
        for k in trivalues:
            if (i == j) & (i == k):
                print k
                break
