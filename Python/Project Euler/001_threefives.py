results = []

for i in range(1000): 
    if i % 3 == 0:
       results.append(i)
    elif i % 5 == 0:
        results.append(i)
    else:
        continue

s = sum(results)

print(s)
