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

    window.mainloop()

##  Populate the screen with entry fields needed for user array creation
def onCreateArrayClick(window):
    removeVisibleWidgets()
    
    sep = ttk.Separator(window, orient=HORIZONTAL)
    sep.grid(row=1, column=0, padx=(100,20), sticky=EW)

    entry = Entry(window, fg='light grey', relief=FLAT, width=50)
    entry.grid(row=2, column=0, columnspan=2, pady=(10,0))
    entry.insert(0, entryText)
    entry.bind('<FocusIn>', partial(onFocusIn, entry))
    entry.bind('<FocusOut>', partial(onFocusOut, entry))

    clearBtn = Button(window, text='Clear', width=8)
    clearBtn.config(command=partial(onClear, entry))
    clearBtn.grid(row=3, column=0, padx=(0,2), pady=(4,0), sticky=E)

    submitBtn = Button(window, text='Submit', width=8)
    submitBtn.config(command=partial(onSubmit, window, entry))
    submitBtn.grid(row=3, column=1, padx=(2,0), pady=(4,0), sticky=W)

    addVisibleWidgets([sep, entry, clearBtn, submitBtn])

##  Populate the screen with entry fields needed for pre-defined array selection
def onSelectArrayClick(window):
    removeVisibleWidgets()

    sep = ttk.Separator(window, orient=HORIZONTAL)
    sep.grid(row=1, column=1, padx=(20,100), sticky=EW)

    addVisibleWidgets([sep])

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

##  Submit user input
def onSubmit(window, entry):
    entry = entry.get().split(',')
    valid, err = checkEntry(entry)
    displayError(window, valid, err)

    if valid == True:
        ##  Convert entry elements to integers
        for i in range(0, len(entry)):
            entry[i] = int(entry[i])

if __name__ == '__main__':
    main()
