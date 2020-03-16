N = 10000
def bubble_sort1(array):
    n = len(array)

    
    for pass_num in range(n - 1, 0, -1):
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                
def bubble_sort2(array):
    n = len(array)
    t = 1
    start = 0
    for pass_num in range(n - 1, 0, -1):
        start1 = start
        count = 0
        pass_num1 = pass_num
        if t < 0:
            start1, pass_num1 = pass_num1, start1
            start += 1
        for i in range(start1, pass_num1, t):
            if (array[i] > array[i + t] and t > 0) or (array[i + t] > array[i] and t < 0):
                array[i], array[i + t] = array[i + t], array[i]
                count += 1
        if count == 0:
            break
        t = -t

def selection_sort(array):
    n = len(array)
    for i in range(n):
        m = 0
        for j in range(n - i):
            if array[j] > array[m]:
                m = j
        array[n - (i + 1)], array[m] = array[m], array[n - (i + 1)]

        
def insertion_sort(array):
    n = len(array)
    for index in range(1, n):

        current_value = array[index]
        position = index
        while position > 0:
            if array[position - 1] > current_value:
                array[position] = array[position - 1]
            else:
                break
            position -= 1
        array[position] = current_value
