
def sumOfDivisors(n):
    # code here
    sum =0
    for i in range(1, n+ 1):
        sum += (n // i) * i
    return sum

if __name__ == '__main__':
    print(sumOfDivisors(4))