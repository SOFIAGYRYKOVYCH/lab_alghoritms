import math
l= 0
r= 10
eps = 0.000001
m = (r + l) / 2
while r - l >eps:
    if (m ** 3 + m + 1 > 5):
        r = m
    else:
        l = m
    m = (r + l) / 2
print(l)
