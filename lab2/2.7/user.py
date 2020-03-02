def leftbi(array, x):
    l = -1
    lenth = len(array)
    while lenth - l > 1:
        mid = (lenth + l) // 2
        if array[mid] < x:
            l = mid
        else:
            lenth = mid
    return l

def rightbi(array, x):
    l = -1
    lenth = len(array)
    while lenth - l > 1:
        mid = (lenth + l) // 2
        if array[mid] <= x:
            l = mid
        else:
            lenth = mid
    return lenth

def counter(array, x):
   left = leftbi(array,x)
   right = rightbi(array,x)
   nums = right - left -1
   return nums

