
import math

def allDivisors(N):
    sqrt = int(math.sqrt(N))
    l=[]

    for i in range(1, sqrt+1):
        if N%i==0:
            l.append(i)
            if i != N//i:
                l.append(N//i)

    return l

if __name__ == '__main__':
    L = allDivisors(100)
    print(L)
