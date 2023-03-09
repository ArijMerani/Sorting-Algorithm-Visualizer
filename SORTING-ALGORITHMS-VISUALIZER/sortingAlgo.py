from tkinter import *
from tkinter import ttk
import time
import math


root = Tk()
root.title("Sorting Algorithms Visualizer")
root.maxsize(1400, 900)
root.config(bg = "white")
ws = Tk()

algo_name = StringVar()
algo_list = ['Merge Sort' , 'Bubble Sort' , 'Insertion Sort' , 'Heap Sort' , 'Quick Sort' , 'Counting Sort' , 'Radix Sort' , 'Optimized QuickSort' , 'Bucket Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']


arr = []


def displayArr(arr, colorArray):
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
        canvas.create_rectangle(x1, y1, x2, y2, fill=colorArray[i])

    root.update_idletasks()


def createArr():
    global arr
    arr = []
    file_array = open('Array.txt' , "r")
    for i in file_array:
        arr.append(int(i))

    displayArr(arr, ["blue" for x in range(len(arr))])
 

def set_speed():

    slow = 1.5
    medium = 0.04
    fast = 0.0000001

    if speed_comboBox.get() == 'Slow':
        return slow
    elif speed_comboBox.get() == 'Medium':
        return medium
    elif speed_comboBox.get() =="Fast":
        return fast



def merge(arr, begin, mid, end):
    p = begin
    q = mid + 1
    tempArray = []

    for i in range(begin, end+1):
        if p > mid:
            tempArray.append(arr[q])
            q+=1
        elif q > end:
            tempArray.append(arr[p])
            p+=1
        elif arr[p] < arr[q]:
            tempArray.append(arr[p])
            p+=1
        else:
            tempArray.append(arr[q])
            q+=1

    for p in range(len(tempArray)):
        arr[begin] = tempArray[p]
        begin += 1

def merge_sort(arr, begin, end, displayArr, tym):
    if begin < end:
        mid = int((begin + end) / 2)
        merge_sort(arr, begin, mid, displayArr, tym)
        merge_sort(arr, mid+1, end, displayArr, tym)

        merge(arr, begin, mid, end)

        displayArr(arr, ["#71189E" if x >= begin and x < mid else "#A225AD" if x == mid 
                        else "#F381FC" if x > mid and x <=end else "blue" for x in range(len(arr))])
        time.sleep(tym)

    displayArr(arr, ["blue" for x in range(len(arr))])

def heapify(arr, n, i,tym):
    largest = i  
    l = 2 * i + 1  
    r = 2 * i + 2  

 
    if l < n and arr[i] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  
 
        heapify(arr, n, largest,tym)

 
def HeapSort(n,arr,tym):
    n = len(arr)
 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i,tym)
        displayArr(arr, ['green' if x > i else 'yellow' if x==i else 'red' for x in range(n)])
        time.sleep(tym)
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0,tym)

def getColorArray(n, start, end, border,
                  curr_index, isSwaping=False):
    colorArray = []
    for i in range(n):
        if i >= start and i <= end:
            colorArray.append('Grey')
        else:
            colorArray.append('White')
 
        if i == end:
            colorArray[i] = 'Blue'
        elif i == border:
            colorArray[i] = 'Red'
        elif i == curr_index:
            colorArray[i] = 'Yellow'
 
        if isSwaping:
            if i == border or i == curr_index:
                colorArray[i] = 'Green'
 
    return colorArray


def partition(arr, start, end, displayArr, timeTick):
    border = start
    pivot = arr[end]
 
    displayArr(arr, getColorArray(len(arr), start,
                                 end, border, border))
    time.sleep(timeTick)
 
    for j in range(start, end):
        if arr[j] < pivot:
            displayArr(arr, getColorArray(
                len(arr), start, end, border, j, True))
            time.sleep(timeTick)
 
            arr[border], arr[j] = arr[j], arr[border]
            border += 1
 
        displayArr(arr, getColorArray(len(arr), start,
                                     end, border, j))
        time.sleep(timeTick)
 
    # swapping pivot with border value
    displayArr(arr, getColorArray(len(arr), start,
                                 end, border, end, True))
    time.sleep(timeTick)
 
    arr[border], arr[end] = arr[end], arr[border]
 
    return border

def quick_sort(arr, start, end,displayArr, timeTick):
    if start < end:
        partitionkey = partition(arr, start,end, displayArr,timeTick)
 
        quick_sort(arr, start, partitionkey-1,displayArr, timeTick)
 
        quick_sort(arr, partitionkey+1,end, displayArr, timeTick)


def counting_sort(arr, displayArr, tym):
    mval = 0
    for i in range(len(arr)):
        displayArr(arr, ['red' if x == i else ['black'] for x in range(len(arr))])
        time.sleep(tym)
        if arr[i] > mval:
            mval = arr[i]

    buckets = [0 for i in range(mval + 1)]

    for i in arr:
        buckets[i] += 1

    i = 0
    for j in range(mval + 1):
        for _ in range(buckets[j]):
            arr[i] = j
            i += 1

    displayArr(arr, ['blue' for x in range(len(arr))])
    time.sleep(tym)

    return arr

def counting(arr, exp1, displayArr, tym): 

    n = len(arr)

    output = [0] * (n) 
    count = [0] * (10)

    for i in range(0, n):
        index = (arr[i] / exp1) 
        count[int(index % 10)] += 1

    for i in range(1, 10): 
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0: 
        index = (arr[i] / exp1) 
        output[count[int(index % 10)] - 1] = arr[i] 
        count[int(index % 10)] -= 1
        i -= 1

    for i in range(0, len(arr)): 
        arr[i] = output[i]

    displayArr(arr, ['black' for x in range(len(arr))])
    time.sleep(tym)

def radix_sort(arr, displayArr, tym): 


    exp = 1
    numss = len(str(max(arr)))

    while numss != 0: 
        counting(arr, exp, displayArr, tym) 
        exp *= 10
        numss -= 1

    return arr


def bucket_sort(arr,displayArr,tym):
    a=[0.91,0.3,0.53,0.22,0.23,0.76]
    new_arr = []
    for i in range(len(a)):
        new_arr.append([])
    
    k = len(a)
    for i in range(0,k):
        b = int(k* a[i])
        new_arr[b].append(a[i])

    for j in range(0,k):
        new_arr[j] = insertion_sort(new_arr[j],displayArr,tym)

    index=0
    for i in range(0,k):
        for j in range(0,len(new_arr[i])):
            a[index] = new_arr[i][j]
            index = index+1
    displayArr(new_arr,["blue" for x in range(len(new_arr))])
    time.sleep(tym)


def insertion_sort(arr , displayArr,tym):
    for i in range(1, len(arr)):
      
            key = arr[i]
            j = i-1
            while (j >=0 and key < arr[j]):
                arr[j+1] = arr[j]
                j -= 1
                displayArr(arr, ["yellow" if x == j else "red" if x==j+1 else "blue" for x in range(len(arr))])
                time.sleep(tym)
            arr[j+1] = key

            displayArr(arr, ["blue" for x in range(len(arr))])


def optinsertionSort(arr, low, n,displayArr,tym):
    
    for i in range(low+1, n+1):
      
            key = arr[i]
            j = i
            while (j > low and key < arr[j-1]):

                arr[j],arr[j-1] = arr[j-1],arr[j]
                j -= 1
                displayArr(arr, ["orange" if x == j else "black" if x==j+1 else "purple" for x in range(len(arr))])
                time.sleep(tym)
            arr[j] = key

    displayArr(arr, ["blue" for x in range(len(arr))])


def optimizedQuickSort(arr, low, high, k, displayArr, tym):
	while low < high:
		if (high - low) < k:
			optinsertionSort(arr, low, high,displayArr,tym)
			break
		else:
			pivot = partition(arr, low, high,displayArr,tym)
			
			if (pivot - low) < (high - pivot):
				optimizedQuickSort(arr, low, pivot - 1, k,displayArr,tym)
				low = pivot + 1
			else:
				optimizedQuickSort(arr, pivot + 1, high, k,displayArr,tym)			
				high = pivot - 1


def sort():
    tym = set_speed()
    n = len(arr)

    if algo_comboBox.get()=='Merge Sort':
        message ='''
                MERGE SORT:
                Time Complexity: 
                Best Case:Ω(nlog(n))
                Average Case:θ(nlog(n))
                Worst Case:O(nlog(n))
                Space Complexity: O(n)
                '''
        text_box = Text(ws,height=4,width=40)
        text_box.pack(expand=True)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        start = time.time()
        merge_sort(arr, 0, len(arr)-1, displayArr, tym)
        end=time.time()
        print("Merge Sort: ",end-start,"seconds")

    elif algo_comboBox.get()=='Bubble Sort':
        message ='''
                BUBBLE SORT:
                Time Complexity: 
                Best Case:Ω(N)
                Average Case:θ(N^2)
                Worst Case:O(N^2)
                Space Complexity: O(1)
                '''
        text_box = Text(ws,height=4,width=40)
        text_box.pack(expand=True)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        start=time.time()
        for i in range(n-1):
            for j in range(0, n-i-1):
                if (arr[j] > arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  #SWAP

                    displayArr(arr, ["yellow" if x == j else "red" if x==j+1 else "blue" for x in range(len(arr))])
                    time.sleep(tym)
        end=time.time()
        print("Bubble Sort: ",end-start,"seconds")
        displayArr(arr, ["blue" for x in range(len(arr))])
    

    elif algo_comboBox.get()=='Insertion Sort':
        message ='''
                INSERTION SORT:
                Time Complexity: 
                Best Case:Ω(N)
                Average Case:θ(N^2)
                Worst Case:O(N^2)
                Space Complexity: O(1)
                '''
        text_box = Text(ws,height=4,width=40)
        text_box.pack(expand=True)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        start=time.time()
        for i in range(1, len(arr)):
      
            key = arr[i]
            j = i-1
            while (j >=0 and key < arr[j]):

                arr[j+1] = arr[j]
                j -= 1
                
                displayArr(arr, ["yellow" if x == j else "red" if x==j+1 else "blue" for x in range(len(arr))])
                time.sleep(tym)
            arr[j+1] = key
        end=time.time()
        print("Insertion Sort: ",end-start,"seconds")
        displayArr(arr, ["blue" for x in range(len(arr))])
    
    elif algo_comboBox.get()=='Heap Sort':
        message ='''
                HEAP SORT:
                Time Complexity: 
                Best Case:Ω(nlog(n))
                Average Case:θ(nlog(n))
                Worst Case:O(nlog(n))
                Space Complexity: O(1)
                '''
        text_box = Text(ws,height=4,width=40)
        text_box.pack(expand=True)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        start=time.time()
        HeapSort(n,arr,tym)
        end=time.time()
        print("Heap Sort: ",end-start,"seconds")
        displayArr(arr, ['blue' for x in range(len(arr))])


    elif algo_comboBox.get()=='Quick Sort':
        message ='''
                QUICK SORT:
                Time Complexity: 
                Best Case:Ω(nlog(n))
                Average Case:θ(nlog(n))
                Worst Case:O(n^2)
                Space Complexity: O(n)
                '''
        text_box = Text(ws,height=4,width=40)
        text_box.pack(expand=True)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        start=time.time()
        quick_sort(arr,0,len(arr)-1,displayArr, tym)
        end=time.time()
        print("Quick Sort: ",end-start,"seconds")
        displayArr(arr , ['Blue' for x in range(len(arr))])

    elif algo_comboBox.get()=='Counting Sort':
        message ='''
                COUNTING SORT:
                Time Complexity: 
                Best Case:Ω(n+k)
                Average Case:θ(n+k)
                Worst Case:O(n+k)
                Space Complexity: O(k)
                '''
        text_box = Text(ws,height=4,width=40)
        text_box.pack(expand=True)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        start=time.time()
        counting_sort(arr,displayArr,tym)
        end=time.time()
        print("Counting Sort: ",end-start,"seconds")

    elif algo_comboBox.get()=='Radix Sort':
        message ='''
                RADIX SORT:
                Time Complexity: 
                Best Case:Ω(nk)
                Average Case:θ(nk)
                Worst Case:O(nk)
                Space Complexity: O(n+k)
                '''
        text_box = Text(ws,height=4,width=40)
        text_box.pack(expand=True)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        start=time.time()
        radix_sort(arr,displayArr,tym)
        end=time.time()
        print("Radix Sort: ",end-start,"seconds")
        displayArr(arr , ['Blue' for x in range(len(arr))])

    elif algo_comboBox.get()=='Bucket Sort':
        message ='''
                BUCKET SORT:
                Time Complexity: 
                Best Case:Ω(n+k)
                Average Case:θ(n+k)
                Worst Case:O(n^2)
                Space Complexity: O(n)
                '''
        text_box = Text(ws,height=4,width=40)
        text_box.pack(expand=True)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        sorted_arr = bucket_sort(arr,displayArr,tym)
        start=time.time()
        displayArr(sorted_arr , ['Blue' for x in range(len(sorted_arr))])   
        end=time.time()
        # print("Bucket Sort: ",end-start,"seconds")
    elif algo_comboBox.get()=='Optimized QuickSort':
        message ='''
                OPTIMIZED QUICK SORT:
                Time Complexity:
                O(nk + nlog(n/k))
                Space Complexity: O(n)
                '''
        text_box = Text(ws,height=4,width=40)
        text_box.pack(expand=True)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        n = len(arr)
        k  = math.floor(math.log2(n))
        start=time.time()
        optimizedQuickSort(arr,0,n-1 ,k,displayArr,tym)
        end=time.time()
        print("Optimized QuickSort: ",end-start,"seconds")
        displayArr(arr , ['Blue' for x in range(len(arr))])    

    

display_window = Frame(root, width= 900, height=300, bg="blue")
display_window.grid(row=0, column=0, padx=10, pady=5)


lbl1 = Label(display_window, text="Algorithm: ", bg="white")
lbl1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_comboBox = ttk.Combobox(display_window, textvariable=algo_name, values=algo_list)
algo_comboBox.grid(row=0, column=1, padx=5, pady=5)
algo_comboBox.current(0)


lbl2 = Label(display_window, text="Sorting Speed: ", bg="white")
lbl2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_comboBox = ttk.Combobox(display_window, textvariable=speed_name, values=speed_list)
speed_comboBox.grid(row=1, column=1, padx=5, pady=5)
speed_comboBox.current(0)


btn1 = Button(display_window, text="Sort", command=sort, bg="#C4C5BF")
btn1.grid(row=4, column=1, padx=5, pady=5)


btn2 = Button(display_window, text="Create Array", command=createArr, bg="#C4C5BF")
btn2.grid(row=4, column=0, padx=5, pady=5)


canvas = Canvas(root, width=800, height=400, bg="white")
canvas.create_text(300, 50, text="SORTING ALGORITHMS", fill="black", font=('Helvetica 15 bold'))
canvas.grid(row=1, column=0, padx=10, pady=5)



ws.mainloop()
root.mainloop()