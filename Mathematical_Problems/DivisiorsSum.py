
'''
https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1
'''


def sumOfDivisors(n):
    # code here
    sum =0
    for i in range(1, n+ 1):
        sum += (n // i) * i
    return sum

if __name__ == '__main__':
    print(sumOfDivisors(4))