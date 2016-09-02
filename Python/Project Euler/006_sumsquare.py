"""
results = 0
for i in range(1,101):
    for j in range(1,101):
        results += i*j

for k in range(1,101):
    results -= k**2
print(results)
"""

n = 100
a = n*(n+1)/2
b = (2*n+1)*(n+1)*n/6

r = a^2+b
print(r)
