N = 1000000
def quick_sort(array, key=lambda a: a):
    quick_sort_helper(array, 0, len(array) - 1, key)


def quick_sort_helper(array, first, last, key=lambda a: a):
    if first < last:
        splitpoint = partition(array, first, last, key)
        quick_sort_helper(array, first, splitpoint - 1, key)
        quick_sort_helper(array, splitpoint + 1, last, key)


def partition(array, first, last, key=lambda a: a):
    pivot = array[first]
    left = first + 1
    right = last
    done = False
    while not done:
        while left <= right and key(array[left]) <= key(pivot):
            left += 1
        while key(array[right]) >= key(pivot) and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            array[left], array[right] = array[right], array[left]
    array[first], array[right] = array[right], array[first]
    return right
