import time
import numpy as np

def bisect(f,a,b,S,T):
    if np.sign(np.polyval(f,a)) == np.sign(np.polyval(f,b)):
        print "\nError: f(a) and f(b) have the same signs."
    else:
        i = 0
        while i <= S:
            e = b - a
            e /= 2
            c = a + e
            if abs(np.polyval(f,c)) < T:
                print "\nThe solution is %d. The computation was a success after %d iterations!\n\n" % (c,i)
                break
            i += 1
            if np.sign(np.polyval(f,a)) == np.sign(np.polyval(f,c)):
                a = c
            else:
                b = c 
        if i == S+1:
            print "\nMethod failed after %d iterations.\n\n" % (S)
