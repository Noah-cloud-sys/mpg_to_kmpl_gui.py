# Program Name: mpgtokmpl.py 
# Course: IT3883/Section XXX
# Student Name: David Touchstone
# Assignment Number: Lab#3
# Due Date: 02/23/ 2025
# Purpose: This is to act as a calculator and allow someone to translate MPG to KMPL without having to hit the update button each time.
# List Specific resources used to complete the assignment. - https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/, https://docs.python.org/3/library/tkinter.html, https://www.activestate.com/resources/quick-reads/how-to-create-a-calculator-in-python-tkinter/



import tkinter as tk
from tkinter import StringVar

def convert_mpg_to_kmpl(*_):
    try:
        kmpl_value = float(mpg_var.get()) * 0.425143707
        result_var.set(f"{kmpl_value:.4f} km/L")
    except ValueError:
        result_var.set("Invalid input")

# User interface Loadout
root = tk.Tk()
root.title("Miles Per Gallon to Kilometer per Liter Converter")
root.geometry("200x200")

#input and output var
mpg_var, result_var = StringVar(), StringVar()
mpg_var.trace("w", convert_mpg_to_kmpl)

# Loadout Details
tk.Label(root, text="Enter Miles Per Gallon:").pack(pady=10)
tk.Entry(root, textvariable=mpg_var).pack(pady=10)
tk.Label(root, textvariable=result_var, font=("New Times Roman", 25)).pack(pady=10)

# loop for automatic updates
root.mainloop()
