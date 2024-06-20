
# using Log base 10
import math

n = int(input())
ans = math.floor(math.log10(n))+1 if n!=0 else 1
print(ans)