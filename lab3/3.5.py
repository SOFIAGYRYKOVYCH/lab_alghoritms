import math
l = 0 
r = 2
m = (r + l) / 2
eps = 0.0000000001
while r != m and l != m:
    if (m ** 3 + 4 * m * m + m > 6):
        r = m
    else:
        l = m
    m = (r + l) / 2
print(l)
