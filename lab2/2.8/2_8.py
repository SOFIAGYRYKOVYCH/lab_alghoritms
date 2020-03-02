from math import  log2
def powchek(x):
    a = log2(x)
    if  a != 0 and a % 1 == 0 :
        return 1
    else :
        return 0
    
pos = []
arr  = [1,2,3,4,5,8,16,64,129]
for i in range(len(arr)):
    checker = powchek(arr[i])
    if checker == 1:
        pos.append(i)
        print("Yes", end = ' ')
    else:
        print("No" , end = ' ')
print(pos) # вывод номеров 2
'''O(n) - асимптотика'''
