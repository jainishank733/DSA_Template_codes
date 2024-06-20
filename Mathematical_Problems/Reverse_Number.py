
x = int(input())

# flag var to check '-ve' or '+ve'
sign = 1
if x < 0:
    sign = -1
    x = -1 * x

# reverse number store variable
revNum = 0

# iterate till x == 0
while x > 0:
    revNum = revNum * 10 + x % 10
    x //= 10

# return reverse number along with sign
ans = sign * revNum

print(ans)