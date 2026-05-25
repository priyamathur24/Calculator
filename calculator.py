import tkinter as tk
from tkinter import *
import math

# Create window
root = Tk()
root.title("Scientific Calculator")
root.geometry("500x650")
root.configure(bg="black")

# Entry field
equation = StringVar()

entry = Entry(
    root,
    textvariable=equation,
    font=("Arial", 24),
    bd=10,
    relief=RIDGE,
    justify="right",
    bg="white"
)

entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=25, pady=10)

# Function to insert values
def press(num):
    current = equation.get()
    equation.set(current + str(num))

# Function to clear
def clear():
    equation.set("")

# Function to calculate
def equal():
    try:
        expr = equation.get()

        # Replace symbols
        expr = expr.replace('π', str(math.pi))
        expr = expr.replace('√', 'math.sqrt')
        expr = expr.replace('sin', 'math.sin')
        expr = expr.replace('cos', 'math.cos')
        expr = expr.replace('tan', 'math.tan')
        expr = expr.replace('log', 'math.log10')

        result = eval(expr)
        equation.set(result)

    except:
        equation.set("Error")

# Scientific functions
def square():
    try:
        value = float(entry.get())
        equation.set(value ** 2)
    except:
        equation.set("Error")

def cube():
    try:
        value = float(entry.get())
        equation.set(value ** 3)
    except:
        equation.set("Error")

def inverse():
    try:
        value = float(entry.get())
        equation.set(1 / value)
    except:
        equation.set("Error")

# Buttons list
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3), ('C', 2, 4),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3), ('(', 3, 4),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3), (')', 4, 4),
    ('0', 5, 0), ('.', 5, 1), ('%', 5, 2), ('+', 5, 3), ('=', 5, 4),
    ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3), ('π', 6, 4),
    ('√(', 7, 0), ('x²', 7, 1), ('x³', 7, 2), ('1/x', 7, 3)
]

# Create buttons
for (text, row, col) in buttons:

    if text == '=':
        btn = Button(root, text=text, width=8, height=3,
                     font=("Arial", 14), bg="orange",
                     command=equal)

    elif text == 'C':
        btn = Button(root, text=text, width=8, height=3,
                     font=("Arial", 14), bg="red",
                     command=clear)

    elif text == 'x²':
        btn = Button(root, text=text, width=8, height=3,
                     font=("Arial", 14), bg="gray",
                     command=square)

    elif text == 'x³':
        btn = Button(root, text=text, width=8, height=3,
                     font=("Arial", 14), bg="gray",
                     command=cube)

    elif text == '1/x':
        btn = Button(root, text=text, width=8, height=3,
                     font=("Arial", 14), bg="gray",
                     command=inverse)

    else:
        btn = Button(root, text=text, width=8, height=3,
                     font=("Arial", 14), bg="lightblue",
                     command=lambda t=text: press(t))

    btn.grid(row=row, column=col, padx=5, pady=5)

# Run application
root.mainloop()