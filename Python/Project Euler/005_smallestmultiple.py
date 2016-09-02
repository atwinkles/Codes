'''
results = []
results2 = []
for i in range(1,10000000):
    for j in range(1,21):
        if i % j == 0:
            results.append(i)
        else:
            continue
    
    if results.count(i) == 20:
        results2.append(i)
r = min(results2)
#print(results)
print(r)
'''

answer = 2*2*2*2*3*3*5*7*11*13*17*19
print(answer)
