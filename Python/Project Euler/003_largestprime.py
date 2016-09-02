import numpy as np

i = 600851475143

results = []

for j in range(2,int(np.sqrt(i))):
    while i % j == 0:
        i = i/j
        if results.count(j) == True:
            continue
        else:
            results.append(j)

r = max(results)
print(r)
