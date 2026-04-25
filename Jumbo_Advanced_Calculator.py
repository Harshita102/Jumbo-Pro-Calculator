from tkinter import *
import math
import matplotlib.pyplot as plt
import re

# ---------------- WINDOW ----------------
root = Tk()
root.title("Jumbo Advanced Calculator")
root.geometry("1000x600")
root.configure(bg="black")

expression = ""
memory = 0

# ---------------- DISPLAY ----------------
entry = Entry(root, font=("Arial", 24), bg="#111", fg="white",
              bd=5, relief=FLAT, justify="right")
entry.place(x=20, y=20, width=650, height=60)

# ---------------- HISTORY ----------------
history = Listbox(root, bg="#111", fg="lightgreen", font=("Arial", 10))
history.place(x=700, y=20, width=260, height=400)

# ---------------- FIX EXPRESSION ----------------
def fix_expression(exp):
    exp = exp.replace("π", str(math.pi))
    exp = exp.replace("e", str(math.e))

    # implicit multiplication fix (2π, 2sin, etc.)
    exp = re.sub(r'(\d)([a-zA-Z\(])', r'\1*\2', exp)

    exp = exp.replace("^", "**")

    exp = exp.replace("sin(", "math.sin(math.radians(")
    exp = exp.replace("cos(", "math.cos(math.radians(")
    exp = exp.replace("tan(", "math.tan(math.radians(")
    exp = exp.replace("log(", "math.log10(")
    exp = exp.replace("ln(", "math.log(")
    exp = exp.replace("√(", "math.sqrt(")
    exp = exp.replace("fact(", "math.factorial(")

    return exp

# ---------------- CALCULATE ----------------
def calculate():
    global expression
    try:
        exp = fix_expression(expression)

        result = eval(exp)

        history.insert(END, f"{expression} = {result}")

        entry.delete(0, END)
        entry.insert(0, result)
        expression = str(result)

    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")
        expression = ""

# ---------------- BASIC ----------------
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

def add_func(f):
    press(f + "(")

# ---------------- MEMORY ----------------
def mc():
    global memory
    memory = 0

def mr():
    press(str(memory))

def mplus():
    global memory
    try:
        memory += float(entry.get())
    except:
        pass

def mminus():
    global memory
    try:
        memory -= float(entry.get())
    except:
        pass

# ---------------- GRAPH ----------------
def graph():
    try:
        x = list(range(-10, 11))
        exp = fix_expression(expression)
        y = [eval(exp.replace("x", str(i))) for i in x]

        plt.plot(x, y)
        plt.title("Graph")
        plt.grid()
        plt.show()

    except:
        entry.delete(0, END)
        entry.insert(0, "Graph Error")

# ---------------- CONVERTER ----------------
def converter():
    try:
        val = float(entry.get())
        result = val * 1000   # km → m example
        entry.delete(0, END)
        entry.insert(0, f"{result} m")
    except:
        entry.delete(0, END)
        entry.insert(0, "Conv Error")

# ---------------- BUTTON ----------------
def btn(t,x,y,cmd,color="#333"):
    Button(root,text=t,command=cmd,bg=color,fg="white",
           font=("Arial",12),bd=0).place(x=x,y=y,width=80,height=50)

# ---------------- MEMORY ----------------
btn("MC",20,100,mc)
btn("MR",110,100,mr)
btn("M+",200,100,mplus)
btn("M-",290,100,mminus)

# ---------------- SCI ----------------
btn("sin",380,100,lambda:add_func("sin"))
btn("cos",470,100,lambda:add_func("cos"))
btn("tan",560,100,lambda:add_func("tan"))

btn("log",380,160,lambda:add_func("log"))
btn("ln",470,160,lambda:add_func("ln"))
btn("exp",560,160,lambda:press("e**"))

# ---------------- NUMBERS ----------------
nums=[('7',20,220),('8',110,220),('9',200,220),
      ('4',20,280),('5',110,280),('6',200,280),
      ('1',20,340),('2',110,340),('3',200,340),
      ('0',20,400)]

for (t,x,y) in nums:
    btn(t,x,y,lambda v=t:press(v))

# ---------------- OPERATORS ----------------
btn("/",290,220,lambda:press("/"))
btn("*",290,280,lambda:press("*"))
btn("-",290,340,lambda:press("-"))
btn("+",290,400,lambda:press("+"))

btn("=",110,400,calculate,"green")

# ---------------- EXTRA ----------------
btn("√",380,220,lambda:add_func("√"))
btn("x²",470,220,lambda:press("**2"))
btn("x³",560,220,lambda:press("**3"))

btn("(",380,280,lambda:press("("))
btn(")",470,280,lambda:press(")"))
btn("π",560,280,lambda:press("π"))

btn("fact",380,340,lambda:add_func("fact"))
btn("C",470,340,clear,"#555")
btn("CE",560,340,backspace,"red")

# ---------------- SIDE ----------------
Button(root,text="Graph",bg="blue",fg="white",
       command=graph).place(x=700,y=440,width=260,height=50)

Button(root,text="Converter",bg="green",fg="white",
       command=converter).place(x=700,y=500,width=260,height=50)

# ---------------- RUN ----------------
root.mainloop()

