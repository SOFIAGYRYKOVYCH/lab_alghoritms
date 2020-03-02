import math
l = 1.6
r = 3
m = (r + l) / 2
eps=0.000000001
while r - l > eps:
    if (3 * math.sin(m) - m < 0):
        r = m
    else:
        l = m
    m = (r + l) / 2
print(l)
 
