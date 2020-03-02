def bsearch_rightmost(array, x):
    low = 0
    t  = True
    high = len(array) - 1
    if x > array[-1]  :
        return -1
    if array[0] == array[-1] :
        return high
    while low <= high :
        mid = (high + low) // 2
        h = array[mid]
        if h == x :
            while True :
                if not h == array[-1] and h == array[mid+1] :
                    mid+=1
                else :
                    return mid
        elif h > x :
            high = mid - 1

        else :
            low = mid + 1

    return high
                
                
                
            
