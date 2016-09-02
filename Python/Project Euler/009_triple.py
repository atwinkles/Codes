for a in range(0,700):
    for b in range(0,700):
        for c in range(0,700):
            if a + b + c == 1000 and (a**2) + (b**2) == (c**2):
                print(a*b*c)
                break
