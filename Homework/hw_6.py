unsorted = [9, 6, 5, 3, 8, 7,1, 2, 4]
def bubble_sort(list):
    length = len(list)
    for i in range(length):
        for k in range(0, length-i-1):
            if list[k] > list[k+1]:
                list[k], list[k+1] = list[k+1], list[k]
    return list

sorted = bubble_sort(unsorted)
print(sorted)

def binary_search(Val, sorted):
    pos = 0
    ResultOk = False
    first =0
    last = len(sorted)-1
    while first <= last:
        middle = (first + last)//2
        if Val == sorted[middle]:
            first = middle
            last = first -1
            ResultOk = True
            pos = middle

        elif  Val > sorted[middle]:
            first = middle + 1
        else:
            last = middle - 1
    if ResultOk:
        print(f'Element found at position {pos}')
    else:
        print(f'Element not found')

binary_search(9, sorted)


