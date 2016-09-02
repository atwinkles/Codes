def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

result = []

for i in range(1000):
    if fib(i) < 4000000:
        if fib(i) % 2 == 0:
            result.append(fib(i)) 
    else:
        break
r = sum(result)
print(r)
