import random
def search(array, x):
    for i in range(len(array)) :
        if x <= array[i] :
            return i
    return -1

array = [1,2,3,4,6,10]
x = random.randint(0,10)
print(x)
print(search(array,x))
