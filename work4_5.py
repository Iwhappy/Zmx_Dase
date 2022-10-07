import random
import math
def f(x):
    return x**3 + x**2
S = (1.0 - 0.0) * 2
N = 10000000
C = 0
for i in range(N):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 2.0)
    if y <= f(x):
        C += 1
I = C * S / N
print(I)
