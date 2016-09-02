import math

count = 0

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    else:
        return True

for i in range (2,20000000):
    if is_prime(i):
        count += 1
    if count == 10001:
        print(i)
        break
