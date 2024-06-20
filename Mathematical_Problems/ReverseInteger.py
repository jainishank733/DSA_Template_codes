'''
https://leetcode.com/problems/reverse-integer/
'''


def reverse(x):

    # flag var to check '-ve' or '+ve'
    sign = -1 if x<0 else 1

    # reverse number store variable
    revNum = 0

    # iterate till x == 0
    while x!=0:
        revNum = revNum*10 + x%10
        x//=10

    # return reverse number along with sign
    return sign*revNum


if __name__ == '__main__':
    print(reverse(1001))





