
def binrec(array , x , higher  , lower):
    if higher >= lower :
        mid = (higher  + lower) // 2
        h = array[mid]
        if x == h :
            return mid
        if x < h : return binrec(array , x , mid - 1 , lower)
        return binrec(array , x , higher , mid + 1)
    return -1

arr = [1,2,3,4,5,6,7]
x1 = 7
print(binrec(arr,x1,len(arr)-1,0))
