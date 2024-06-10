# gui_calculator.py
# Import necessary modules from tkinter for GUI and math for calculations
import tkinter as tk
from tkinter import messagebox
import math

# Function to handle button clicks
def click(event):
    # Get the text of the clicked button
    text = event.widget.cget("text")
    # If '=' button is clicked, evaluate the expression in the screen
    if text == "=":
        try:
            # Evaluate the expression and display the result
            result = eval(screen.get())
            screen.delete(0, tk.END)
            screen.insert(tk.END, str(result))
        except Exception as e:
            # Show an error message for invalid input
            messagebox.showerror("Error", "Invalid input")
            screen.delete(0, tk.END)
     # If 'C' button is clicked, clear the screen
    elif text == "C":
        screen.delete(0, tk.END)
    else:
         # For other buttons, append the button text to the screen
        screen.insert(tk.END, text)


# Function to calculate the square root
def square_root():
    try:
        # Get the number from the screen and calculate the square root
        number = float(screen.get())
        result = math.sqrt(number)
        screen.delete(0, tk.END)
        screen.insert(tk.END, str(result))
    except Exception as e:
        # Show an error message for invalid input
        messagebox.showerror("Error", "Invalid input")
        screen.delete(0, tk.END)

# Function to prepare for exponentiation
def exponentiate():
    try:
        # Get the number from the screen and prepare for exponentiation
        number = float(screen.get())
        screen.delete(0, tk.END)
        screen.insert(tk.END, str(number) + "**")
    except Exception as e:
         # Show an error message for invalid input
        messagebox.showerror("Error", "Invalid input")
        screen.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Create the display screen
screen = tk.Entry(root, font="Arial 20", borderwidth=2, relief="solid")
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# List of button labels
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+', 
    'C', 'sqrt', 'exp'
]

# Initialize row and column counters
row = 0
col = 0

# Create buttons and place them in the grid
for button in buttons:
    btn = tk.Button(button_frame, text=button, font="Arial 18", relief="solid", borderwidth=1)
    btn.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1
# Create the square root button and place it in the main window
sqrt_btn = tk.Button(root, text="√", font="Arial 18", relief="solid", borderwidth=1, command=square_root)
sqrt_btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)

# Create the exponentiation button and place it in the main window
exp_btn = tk.Button(root, text="x^y", font="Arial 18", relief="solid", borderwidth=1, command=exponentiate)
exp_btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)

# Start the main event loop
root.mainloop()
