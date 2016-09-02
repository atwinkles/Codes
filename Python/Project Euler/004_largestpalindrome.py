results = []

for j in range(1000):
    for k in range(1000):
        if str(j*k) == str(j*k)[::-1]:
            results.append(j*k)

r = max(results)

print(r)
