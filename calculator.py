# gui_calculator.py
import tkinter as tk
from tkinter import messagebox
import math

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.delete(0, tk.END)
            screen.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            screen.delete(0, tk.END)
    elif text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)

def square_root():
    try:
        number = float(screen.get())
        result = math.sqrt(number)
        screen.delete(0, tk.END)
        screen.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input")
        screen.delete(0, tk.END)

def exponentiate():
    try:
        number = float(screen.get())
        screen.delete(0, tk.END)
        screen.insert(tk.END, str(number) + "**")
    except Exception as e:
        messagebox.showerror("Error", "Invalid input")
        screen.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

screen = tk.Entry(root, font="Arial 20", borderwidth=2, relief="solid")
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+', 
    'C', 'sqrt', 'exp'
]

row = 0
col = 0

for button in buttons:
    btn = tk.Button(button_frame, text=button, font="Arial 18", relief="solid", borderwidth=1)
    btn.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

sqrt_btn = tk.Button(root, text="√", font="Arial 18", relief="solid", borderwidth=1, command=square_root)
sqrt_btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)

exp_btn = tk.Button(root, text="x^y", font="Arial 18", relief="solid", borderwidth=1, command=exponentiate)
exp_btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)

root.mainloop()
