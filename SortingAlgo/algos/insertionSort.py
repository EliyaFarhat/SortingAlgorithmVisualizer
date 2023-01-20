import time
from colours import *

def insertionSort(data, drawData, timeTick):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        drawData(data, [DARK_BLUE if x == i else YELLOW if x == j else PURPLE if x < i else RED for x in range(len(data))])
        data[j + 1] = key
        time.sleep(timeTick)
    drawData(data, [PURPLE for x in range(len(data))])