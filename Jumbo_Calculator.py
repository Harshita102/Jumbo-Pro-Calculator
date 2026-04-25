from tkinter import *
import math

# ---------------- WINDOW ----------------
root = Tk()
root.title("Jumbo Calculator")
root.geometry("420x650")
root.configure(bg="#2b2b2b")

expression = ""

# ---------------- DISPLAY ----------------
entry = Entry(root, font=("Arial", 24), bd=10, relief=FLAT,
              justify="right", bg="white")
entry.grid(row=0, column=0, columnspan=5, sticky="nsew", ipady=20, padx=10, pady=10)

# ---------------- FUNCTIONS ----------------
def press(val):
    global expression
    expression += str(val)
    entry.delete(0, END)
    entry.insert(0, expression)

def clear():
    global expression
    expression = ""
    entry.delete(0, END)

def backspace():
    global expression
    expression = expression[:-1]
    entry.delete(0, END)
    entry.insert(0, expression)

def equal():
    global expression
    try:
        exp = expression



        # ---- AUTO MULTIPLY FIX ----
        exp = exp.replace("sin(", "*math.sin(math.radians(")
        exp = exp.replace("cos(", "*math.cos(math.radians(")
        exp = exp.replace("tan(", "*math.tan(math.radians(")

        exp = exp.replace("log(", "*math.log10(")
        exp = exp.replace("ln(", "*math.log(")
        exp = exp.replace("√(", "*math.sqrt(")

        # Remove starting * if exists
        if exp.startswith("*"):
            exp = exp[1:]

        # Replace π
        exp = exp.replace("π", str(math.pi))

        # ---- CLOSE BRACKETS ----
        open_brackets = exp.count("(")
        close_brackets = exp.count(")")
        exp += ")" * (open_brackets - close_brackets)

        print("Final:", exp)

        result = eval(exp)

        entry.delete(0, END)
        entry.insert(0, result)
        expression = str(result)

    except Exception as e:
        print("Error:", e)
        entry.delete(0, END)
        entry.insert(0, "Error")
        expression = ""

def add_func(func):
    global expression
    expression += func
    entry.delete(0, END)
    entry.insert(0, expression)

# ---------------- BUTTON STYLE ----------------
btn_color = "#3c3f41"
fg_color = "white"

def create_btn(text, row, col, cmd, bg=btn_color):
    Button(root, text=text, bg=bg, fg=fg_color,
           font=("Arial", 14), bd=0,
           command=cmd).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# ---------------- BUTTONS ----------------

# Row 1
create_btn("(",1,0,lambda: press("("))
create_btn(")",1,1,lambda: press(")"))
create_btn("%",1,2,lambda: press("%"))
create_btn("CE",1,3,backspace)
create_btn("C",1,4,clear,"red")

# Row 2
create_btn("7",2,0,lambda: press("7"))
create_btn("8",2,1,lambda: press("8"))
create_btn("9",2,2,lambda: press("9"))
create_btn("/",2,3,lambda: press("/"))
create_btn("√",2,4,lambda: add_func("√("))

# Row 3
create_btn("4",3,0,lambda: press("4"))
create_btn("5",3,1,lambda: press("5"))
create_btn("6",3,2,lambda: press("6"))
create_btn("*",3,3,lambda: press("*"))
create_btn("-",3,4,lambda: press("-"))

# Row 4
create_btn("1",4,0,lambda: press("1"))
create_btn("2",4,1,lambda: press("2"))
create_btn("3",4,2,lambda: press("3"))
create_btn("+",4,3,lambda: press("+"))
create_btn("1/x",4,4,lambda: press("1/("))

# Row 5
create_btn("+/-",5,0,lambda: press("-"))
create_btn("0",5,1,lambda: press("0"))
create_btn(".",5,2,lambda: press("."))
create_btn("=",5,3,equal,"green")
create_btn("π",5,4,lambda: press("π"))

# Row 6 (Scientific)
create_btn("sin",6,0,lambda: add_func("sin("))
create_btn("cos",6,1,lambda: add_func("cos("))
create_btn("tan",6,2,lambda: add_func("tan("))
create_btn("log",6,3,lambda: add_func("log("))
create_btn("ln",6,4,lambda: add_func("ln("))

# ---------------- GRID ----------------
for i in range(7):
    root.rowconfigure(i, weight=1)

for i in range(5):
    root.columnconfigure(i, weight=1)

root.mainloop()

