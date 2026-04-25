from tkinter import *

# window create
root = Tk()
root.title("Calculator")
root.geometry("350x500")   # 👈 size increase

# make grid expandable 👇 (VERY IMPORTANT)
for i in range(6):
    root.rowconfigure(i, weight=1)

for i in range(4):
    root.columnconfigure(i, weight=1)

# input field
entry = Entry(root, font=("Arial", 20), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")  # 👈 stretch

# function to click numbers
def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(num))

# clear function
def clear():
    entry.delete(0, END)

# calculate result
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")
# buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

# create buttons
for (text, row, col) in buttons:
    if text == 'C':
        Button(root, text=text, command=clear).grid(row=row, column=col, sticky="nsew")
    elif text == '=':
        Button(root, text=text, command=equal).grid(row=row, column=col, sticky="nsew")
    else:
        Button(root, text=text, command=lambda t=text: click(t)).grid(row=row, column=col, sticky="nsew")

root.mainloop()