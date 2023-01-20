import time
from colours import *

def partition(data, drawData, low, high):
    pivot = data[high]

    i = low - 1
    for j in range(low, high):
        if data[j] <= pivot:

            i = i + 1

            (data[i], data[j]) = (data[j], data[i])
            drawData(data, [BLUE if x < pivot and x >= low else LIGHT_GREEN if x == pivot else RED if x == data[j] else PURPLE for x in range(len(data))])

    (data[i+1], data[high]) = (data[high], data[i+1])

    return i + 1

def quickSort(data, drawData, low, high, timeTick):
    if low < high:
        pi = partition(data, drawData, low, high)
        quickSort(data, drawData, low, pi - 1, timeTick)
        quickSort(data, drawData, pi + 1, high, timeTick)
        time.sleep(timeTick)
    drawData(data, [PURPLE for x in range(len(data))])