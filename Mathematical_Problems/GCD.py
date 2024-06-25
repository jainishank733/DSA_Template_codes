
'''
https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1
'''


'''
Approach: The Euclidean Algorithm is a method for finding the greatest common divisor of two numbers. It operates on the principle that the GCD of two numbers remains the same even if the smaller number is subtracted from the larger number.
'''

def gcd(a,b):
    if a==0:
        return b
    if b == 0:
        return a
    if a>b:
        return gcd(a-b,b)
    else:
        return gcd(a, b-a)

'''
Second approach:

def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
'''




print(gcd(10,6))