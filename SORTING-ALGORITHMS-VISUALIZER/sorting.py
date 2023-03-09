#!/usr/bin/python

from tkinter import *
# from tkinter import ttk
import time
import random
from functools import partial
top = Tk()

arr =[]
def display_array(arr,color_array):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    width_x = canvas_width / (len(arr) + 1)
    ini = 4
    space = 2
    tempArr = [i / max(arr) for i in arr]

    for i in range(len(tempArr)):
        x1 = i * width_x + ini + space
        y1 = canvas_height - tempArr[i] * 390
        x2 = (i + 1) * width_x + ini
        y2 = canvas_height
        canvas.create_rectangle(x1, y1, x2, y2, fill=color_array[i])

    top.update_idletasks()

def Create_Array():
    global arr

    array_size = 25   

    range_begin = 20

    range_end = 150

    arr = []
    for i in range(0, array_size):  
        random_integer = random.randint(range_begin, range_end) #starting from a higher value and not 0 because the vertical bars wont be visible
        arr.append(random_integer)

    display_array(arr, ["blue" for x in range(len(arr))])

window  = Frame(top , width=500 , height = 500 , bg = "white")
window.grid(row=0, column=0, padx=10, pady=5)
window.pack()
algo = Label(window, text="Algorithm: ", bg="white")
algo.grid(row=0, column=0, padx=10, pady=5, sticky=W)
creat_arr = Button(window, text="Create Array", command=Create_Array, bg="#C4C5BF")
creat_arr.grid(row=4, column=1, padx=5, pady=5)


canvas = Canvas(top, width=800, height=400, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

top.mainloop()