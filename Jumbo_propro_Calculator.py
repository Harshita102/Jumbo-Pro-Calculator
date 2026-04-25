import tkinter as tk
from tkinter import messagebox
import math
import matplotlib.pyplot as plt

# ------------------ WINDOW ------------------
root = tk.Tk()
root.title("Jumbo propro Calculator")
root.geometry("900x600")
root.configure(bg="black")

expression = ""
memory = 0
mode = "DEG"

# ------------------ DISPLAY ------------------
entry = tk.Entry(root, font=("Arial", 24), bg="black", fg="white", bd=5, justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# ------------------ FUNCTIONS ------------------

def press(val):
    global expression
    expression += str(val)
    entry.delete(0, tk.END)
    entry.insert(0, expression)

def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

def backspace():
    global expression
    expression = expression[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, expression)

def set_deg():
    global mode
    mode = "DEG"

def set_rad():
    global mode
    mode = "RAD"

# ------------------ SAFE EVAL ------------------
def calculate():
    global expression
    try:
        exp = expression

        # Replace symbols
        exp = exp.replace("π", "pi")
        exp = exp.replace("^", "**")

        # Safe functions
        safe_dict = {
            "sin": lambda x: math.sin(math.radians(x)) if mode=="DEG" else math.sin(x),
            "cos": lambda x: math.cos(math.radians(x)) if mode=="DEG" else math.cos(x),
            "tan": lambda x: math.tan(math.radians(x)) if mode=="DEG" else math.tan(x),
            "log": math.log10,
            "ln": math.log,
            "sqrt": math.sqrt,
            "fact": math.factorial,
            "pi": math.pi,
            "e": math.e,
            "abs": abs,
            "exp": math.exp
        }

        result = eval(exp, {"__builtins__":None}, safe_dict)

        entry.delete(0, tk.END)
        entry.insert(0, result)
        expression = str(result)

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        expression = ""

# ------------------ MEMORY ------------------
def mem_clear():
    global memory
    memory = 0

def mem_recall():
    press(memory)

def mem_add():
    global memory
    try:
        memory += float(entry.get())
    except:
        pass

def mem_sub():
    global memory
    try:
        memory -= float(entry.get())
    except:
        pass

# ------------------ GRAPH ------------------
def plot_graph():
    try:
        x = list(range(-10, 10))
        y = [eval(entry.get().replace("x", str(i))) for i in x]
        plt.plot(x, y)
        plt.title("Graph")
        plt.show()
    except:
        messagebox.showerror("Error", "Invalid function")

# ------------------ CONVERTER ------------------
def converter():
    win = tk.Toplevel(root)
    win.title("Converter")
    win.geometry("300x200")

    tk.Label(win, text="Celsius").pack()
    c = tk.Entry(win)
    c.pack()

    def convert():
        try:
            f = (float(c.get()) * 9/5) + 32
            messagebox.showinfo("Result", f"Fahrenheit: {f}")
        except:
            messagebox.showerror("Error", "Invalid Input")

    tk.Button(win, text="Convert", command=convert).pack()

# ------------------ BUTTON STYLE ------------------
def btn(text, cmd, row, col, colspan=1):
    b = tk.Button(frame, text=text, command=cmd,
                  font=("Arial", 12), bg="#222", fg="white",
                  width=8, height=2)
    b.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)

# ------------------ BUTTON FRAME ------------------
frame = tk.Frame(root, bg="black")
frame.pack()

# Row 1
btn("MC", mem_clear, 0, 0)
btn("MR", mem_recall, 0, 1)
btn("M+", mem_add, 0, 2)
btn("M-", mem_sub, 0, 3)
btn("DEG", set_deg, 0, 4)
btn("RAD", set_rad, 0, 5)

# Row 2
btn("sin", lambda: press("sin("), 1, 0)
btn("cos", lambda: press("cos("), 1, 1)
btn("tan", lambda: press("tan("), 1, 2)
btn("log", lambda: press("log("), 1, 3)
btn("ln", lambda: press("ln("), 1, 4)
btn("exp", lambda: press("exp("), 1, 5)

# Row 3
btn("√", lambda: press("sqrt("), 2, 0)
btn("x²", lambda: press("**2"), 2, 1)
btn("x³", lambda: press("**3"), 2, 2)
btn("xʸ", lambda: press("**"), 2, 3)
btn("1/x", lambda: press("1/("), 2, 4)
btn("|x|", lambda: press("abs("), 2, 5)

# Row 4
btn("π", lambda: press("pi"), 3, 0)
btn("e", lambda: press("e"), 3, 1)
btn("(", lambda: press("("), 3, 2)
btn(")", lambda: press(")"), 3, 3)
btn("%", lambda: press("%"), 3, 4)
btn("fact", lambda: press("fact("), 3, 5)

# Row 5
btn("7", lambda: press("7"), 4, 0)
btn("8", lambda: press("8"), 4, 1)
btn("9", lambda: press("9"), 4, 2)
btn("/", lambda: press("/"), 4, 3)
btn("C", clear, 4, 4)
btn("CE", backspace, 4, 5)

# Row 6
btn("4", lambda: press("4"), 5, 0)
btn("5", lambda: press("5"), 5, 1)
btn("6", lambda: press("6"), 5, 2)
btn("*", lambda: press("*"), 5, 3)
btn("-", lambda: press("-"), 5, 4)

# Row 7
btn("1", lambda: press("1"), 6, 0)
btn("2", lambda: press("2"), 6, 1)
btn("3", lambda: press("3"), 6, 2)
btn("+", lambda: press("+"), 6, 3)

# Row 8
btn("0", lambda: press("0"), 7, 0)
btn(".", lambda: press("."), 7, 1)
btn("=", calculate, 7, 2, 2)

# Tools
tk.Button(root, text="Graph", command=plot_graph, bg="blue", fg="white").pack(pady=5)
tk.Button(root, text="Converter", command=converter, bg="green", fg="white").pack()

# ------------------ RUN ------------------
root.mainloop()
