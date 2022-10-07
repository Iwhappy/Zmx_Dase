import math
print(math.sqrt(2))

low = 0
high = 2
ans = -1
while low <= high:
    mid = (low + high)//2
    if mid **2 <= 2:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1
print(ans)

x = 2
a = x
ex = 0.0000001
while abs( a*a -x) >= ex:
    a = a -(((a * a) - x)/(a *2))
print(a)
