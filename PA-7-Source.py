import random
import tkinter.ttk
from tkinter import *
from functools import partial

visibleWidgets = []
entryText = 'Enter comma-separated list of integers (Ex: 6,2,-5,3)'
errorLbl = None

def main():
    window = Tk()
    window.title("Heap Sort")

    ##  Button for user array creation
    createArrayBtn = Button(window, text='Create an Array', fg='grey50',
                            activeforeground='grey50', cursor='hand2',
                            bd=0, relief=FLAT)
    createArrayBtn.config(command=partial(onCreateArrayClick, window))
    createArrayBtn.grid(row=0, column=0, padx=(100,20))

    ##  Button for pre-defined array selection
    selectArrayBtn = Button(window, text='Select an Array', fg='grey50',
                            activeforeground='grey50', cursor='hand2',
                            bd=0, relief=FLAT)
    selectArrayBtn.config(command=partial(onSelectArrayClick, window))
    selectArrayBtn.grid(row=0, column=1, padx=(20,100))

    ##  Display the array creation tab by default
    onCreateArrayClick(window)

    window.mainloop()

##  Populate the screen with entry fields needed for user array creation
def onCreateArrayClick(window):
    removeVisibleWidgets()

    ##  Underline selected tab
    sep = ttk.Separator(window, orient=HORIZONTAL)
    sep.grid(row=1, column=0, padx=(100,20), sticky=EW)

    ##  User array entry field
    entry = Entry(window, fg='light grey', relief=FLAT, width=50)
    entry.grid(row=2, column=0, columnspan=2, pady=(10,0))
    entry.insert(0, entryText)
    entry.bind('<FocusIn>', partial(onFocusIn, entry))
    entry.bind('<FocusOut>', partial(onFocusOut, entry))

    ##  Clear the entry field
    clearBtn = Button(window, text='Clear', width=8)
    clearBtn.config(command=partial(onClear, entry))
    clearBtn.grid(row=3, column=0, padx=(0,2), pady=(4,0), sticky=E)

    ##  Label the list boxes
    lbl1 = Label(window, text='Before Sorting:', fg='grey50')
    lbl1.grid(row=4, column=0, pady=(70,0))
    lbl2 = Label(window, text='After Sorting:', fg='grey50')
    lbl2.grid(row=4, column=1, pady=(70,0))

    ##  Display the array before sorting
    listboxBefore = Listbox(window)
    scrollbarBefore = Scrollbar(window, orient=VERTICAL)
    listboxBefore.config(yscrollcommand=scrollbarBefore.set)
    scrollbarBefore.config(command=listboxBefore.yview)
    listboxBefore.grid(row=5, column=0, pady=(0,10))
    scrollbarBefore.grid(row=5, column=0, padx=(0,26), pady=(0,10), sticky=E+NS)

    ##  Display the array after sorting
    listboxAfter = Listbox(window)
    scrollbarAfter = Scrollbar(window, orient=VERTICAL)
    listboxAfter.config(yscrollcommand=scrollbarAfter.set)
    scrollbarAfter.config(command=listboxAfter.yview)
    listboxAfter.grid(row=5, column=1, padx=(0,10), pady=(0,10))
    scrollbarAfter.grid(row=5, column=1, padx=(0,36), pady=(0,10), sticky=E+NS)

    ##  Submit user input
    submitBtn = Button(window, text='Submit', width=8)
    submitBtn.config(command=partial(onSubmitCreate, window, entry, listboxBefore, listboxAfter))
    submitBtn.grid(row=3, column=1, padx=(2,0), pady=(4,0), sticky=W)

    ##  Track the currently visible widgets
    addVisibleWidgets([sep, entry, clearBtn, submitBtn, lbl1, lbl2, listboxBefore, scrollbarBefore, listboxAfter, scrollbarAfter])

##  Populate the screen with entry fields needed for pre-defined array selection
def onSelectArrayClick(window):
    removeVisibleWidgets()

    ##  Underline selected tab
    sep = ttk.Separator(window, orient=HORIZONTAL)
    sep.grid(row=1, column=1, padx=(20,100), sticky=EW)

    ##  Generate random arrays
    l1, l2, l3 = generateArrays(-10000, 10000, 10)

    ##  Allow user to select one of the three arrays
    v = IntVar()
    radioBtn1 = Radiobutton(window, text=l1, variable=v, value=0)
    radioBtn1.grid(row=2, column=0, columnspan=2, padx=(40,0), pady=(10,0), sticky=W)
    radioBtn2 = Radiobutton(window, text=l2, variable=v, value=1)
    radioBtn2.grid(row=3, column=0, columnspan=2, padx=(40,0), sticky=W)
    radioBtn3 = Radiobutton(window, text=l3, variable=v, value=2)
    radioBtn3.grid(row=4, column=0, columnspan=2, padx=(40,0), sticky=W)

    ##  Label the list boxes
    lbl1 = Label(window, text='Before Sorting:', fg='grey50')
    lbl1.grid(row=6, column=0, pady=(18,0))
    lbl2 = Label(window, text='After Sorting:', fg='grey50')
    lbl2.grid(row=6, column=1, pady=(18,0))

    ##  Display the array before sorting
    listboxBefore = Listbox(window)
    scrollbarBefore = Scrollbar(window, orient=VERTICAL)
    listboxBefore.config(yscrollcommand=scrollbarBefore.set)
    scrollbarBefore.config(command=listboxBefore.yview)
    listboxBefore.grid(row=7, column=0, pady=(0,10))
    scrollbarBefore.grid(row=7, column=0, padx=(0,26), pady=(0,10), sticky=E+NS)

    ##  Display the array after sorting
    listboxAfter = Listbox(window)
    scrollbarAfter = Scrollbar(window, orient=VERTICAL)
    listboxAfter.config(yscrollcommand=scrollbarAfter.set)
    scrollbarAfter.config(command=listboxAfter.yview)
    listboxAfter.grid(row=7, column=1, padx=(0,10), pady=(0,10))
    scrollbarAfter.grid(row=7, column=1, padx=(0,36), pady=(0,10), sticky=E+NS)

    ##  Submit the user's choice
    submitBtn = Button(window, text='Submit', width=8)
    submitBtn.config(command=partial(onSubmitSelect, window, v, l1, l2, l3, listboxBefore, listboxAfter))
    submitBtn.grid(row=5, column=0, columnspan=2)

    ##  Track the currently visisble widgets
    addVisibleWidgets([sep, radioBtn1, radioBtn2, radioBtn3, submitBtn, lbl1, lbl2, listboxBefore, scrollbarBefore, listboxAfter, scrollbarAfter])

##  Add widgets to global visibleWidgets array
def addVisibleWidgets(widgets):
    for i in widgets:
        visibleWidgets.append(i)

##  Destroy all elements of global visibleWidgets array and empty the array
def removeVisibleWidgets():
    for i in range(len(visibleWidgets), 0, -1):
        visibleWidgets[i-1].destroy()
        visibleWidgets.pop()

##  Remove placeholder text when the user focuses in
def onFocusIn(entry, e):
    if entry.get() == entryText:
        entry.delete(0, END)
    entry.config(fg='black')

##  Replace placeholder text if the user focuses out and no input was given
def onFocusOut(entry, e):
    if entry.get() == '':
        entry.insert(0, entryText)
    entry.config(fg='light grey')

##  Clear array entry
def onClear(entry):
    if entry.get() != entryText:
        entry.delete(0, END)

    if errorLbl != None:
        errorLbl.destroy()

##  Check that the entry is a comma-separated list of valid integers
def checkEntry(entry):
    valid = True
    err = ''

    for i in entry:
        try:
            int(i)
        except:
            valid = False
            err = 'ERROR: Entry must be a list of integers.'
            break

    return valid, err

##  Display error in UI, if there is one
def displayError(window, valid, err):
    global errorLbl
    
    if errorLbl != None:
        errorLbl.destroy()

    if valid == False:
        errVar = StringVar()
        errVar.set(err)

        errorLbl = Label(window, textvariable=errVar, fg='red')
        errorLbl.grid(row=4, column=0, columnspan=2)

##  Create arrays of random numbers
def generateArrays(rangeMin, rangeMax, size):
    l1 = random.sample(range(rangeMin, rangeMax), size)
    l2 = random.sample(range(rangeMin, rangeMax), size)
    l3 = random.sample(range(rangeMin, rangeMax), size)

    return l1, l2, l3

##  Sort the array
def heapSort(array):
    ## Convert array to heap
    length = len(array) - 1
    leastParent = int(length / 2)
    for i in range(leastParent, -1, -1):
        moveDown(array, i, length)

    ## Flatten heap into sorted array
    for i in range(length, 0, -1):
        if array[0] > array[i]:
            swap(array, 0, i)
            moveDown(array, 0, i - 1)

    return array

##  Move an element down
def moveDown(array, first, last):
    largest = 2 * first + 1
    while largest <= last:
        ## Right child exists and is larger than left child
        if (largest < last) and (array[largest] < array[largest + 1]):
            largest += 1

        ##  Right child is larger than parent
        if array[largest] > array[first]:
            swap(array, largest, first)
            ##  Move down to largest child
            first = largest;
            largest = 2 * first + 1
        else:
            return

##  Swap two elements
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

##  Submit user input
def onSubmitCreate(window, entry, listboxBefore, listboxAfter):
    entry = entry.get().split(',')
    valid, err = checkEntry(entry)
    displayError(window, valid, err)

    if valid == True:
        ##  Convert entry elements to integers
        for i in range(0, len(entry)):
            entry[i] = int(entry[i])

        ##  Display original array
        listboxBefore.delete(0, END)
        for i in entry:
            listboxBefore.insert(END, i)

        ##  Run the algorithm
        array = heapSort(entry)

        ##  Display the results
        listboxAfter.delete(0, END)
        for i in array:
            listboxAfter.insert(END, i)

##  Submit user selection
def onSubmitSelect(window, v, l1, l2, l3, listboxBefore, listboxAfter):
    ##  Determine which array the user selected
    v = v.get()
    if v == 0:
        entry = l1
    elif v == 1:
        entry = l2
    else:
        entry = l3

    ##  Display the original array
    listboxBefore.delete(0, END)
    for i in entry:
        listboxBefore.insert(END, i)

    ##  Run the algorithm
    array = heapSort(entry)

    ##  Display the results
    listboxAfter.delete(0, END)
    for i in array:
        listboxAfter.insert(END, i)

if __name__ == '__main__':
    main()
