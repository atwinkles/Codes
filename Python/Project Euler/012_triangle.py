def list_generator(n):
    return [i+1 for i in range(n)]

def triangle_modulo(n):
    count = 0
    for a in list_generator(n):
        count += a
        count2 = 0
        for b in range(1,10000):
            if count % b == 0:
                count2 += 1
            if count2 == 501:
                print(count)
                break

                

triangle_modulo(10000000)
