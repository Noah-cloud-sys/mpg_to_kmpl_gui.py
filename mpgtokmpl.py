import tkinter as tk
from tkinter import StringVar

def convert_mpg_to_kmpl(*args):
    try:
        mpg_value = float(mpg_var.get())
        kmpl_value = mpg_value * 0.425143707
        result_var.set(f"{kmpl_value:.4f} km/L")
    except ValueError:
        result_var.set("Invalid input")

# Create main window
root = tk.Tk()
root.title("MPG to KM/L Converter")
root.geometry("300x150")

# StringVar to hold input and output values
mpg_var = StringVar()
result_var = StringVar()
mpg_var.trace_add("write", convert_mpg_to_kmpl)

# UI Elements
tk.Label(root, text="Enter MPG:").pack(pady=5)
mpg_entry = tk.Entry(root, textvariable=mpg_var)
mpg_entry.pack(pady=5)

result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12))
result_label.pack(pady=10)

# Run application
root.mainloop()
