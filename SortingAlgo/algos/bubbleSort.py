
# Import time module to set speeds for comparisons
import time

# Import colours
from colours import *
from playsound import playsound

def bubble_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(size-1):
        for j in range(size - i -1):
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, [BLUE if x == j or x == j + 1 else RED for x in range(len(data))])
                time.sleep(timeTick)
    drawData(data, [PURPLE for x in range(len(data))])