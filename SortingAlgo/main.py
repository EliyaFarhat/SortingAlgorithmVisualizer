
# Import tkinter to build GUI
from tkinter import *
from tkinter import ttk

# We will need random to create array
import random

# Importing colors from colours.py
from colours import *

# Import algos
from algos.bubbleSort import bubble_sort
from algos.mergeSort import merge_sort
from algos.quickSort import quickSort
from algos.insertionSort import insertionSort

# Creating a basic window
window = Tk()
window.title("Visualization of Sorting Algorithms")
window.maxsize(1500, 900)
window.config(bg=WHITE)


algoName = StringVar()
# Select which algo we want to use
algoList = ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Insertion Sort']

speed = StringVar()
# Select which speed
speedList = ['Fast', 'Medium', 'Slow']

# Empty list that contains the numbers we are going to sort
data = []
counter = 0

# Draws data[] on the canvas as vertical bars
def drawData(data, colourArray):
    canvas.delete("all")
    canvas_width = 1300
    canvas_height = 500
    x_width = canvas_width / (len(data) + 0.6)
    offset = 4
    spacing = 2
    normalizedData = [i/max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 480
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colourArray[i])

    window.update_idletasks()


# This function will generate array with random val each time we click generate
def generate():
    global data

    data = []
    for i in range(0,100):
        random_value = random.randint(1,150)
        data.append(random_value)
    drawData(data, [PURPLE for x in range(len(data))])


# Sets sorting speed


def setSpeed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.000001


# Trigger the algo
def sort():
    global data
    timeTick = setSpeed()

    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quickSort(data, drawData, 0, len(data) - 1, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertionSort(data, drawData, timeTick)



UI_frame = Frame(window, width=1500, height=700, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown for selecting sorting algorithm
list1 = Label(UI_frame, text= "Algorithm: ", bg=WHITE)
list1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algoName, values=algoList)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# dropdown to select sorting speed
l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed, values=speedList)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# sort button
b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

# button for generating array
b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)

# canvas to draw our array
canvas = Canvas(window, width=1300, height=500, bg=LIGHT_GRAY)
canvas.grid(row=1, column=0, padx=10, pady=5)


window.mainloop()
