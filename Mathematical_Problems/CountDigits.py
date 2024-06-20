'''
https://www.geeksforgeeks.org/problems/count-digits5716/1
'''

import math

class CountDigits:
    def evenlyDivides(self, N):

        # calculate number of digits in number
        length = math.floor(math.log10(N)) + 1

        # convert digits in a number to list of digits
        list = [int(i) for i in str(N)]

        # count variable
        count = 0

        for i in range(length):

            # check divisibility of number wrt each digits
            if list[i] != 0 and N % list[i] == 0:
                count += 1

        # return count
        return count


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = CountDigits()
        print(ob.evenlyDivides(N))
# } Driver Code Ends