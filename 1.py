import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = num1 / num2
        else:
            result = "Invalid Operation"

        result_label.config(text="Result: " + str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Basic Calculator")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

operation_var = tk.StringVar(value="Add")
operations = ["Add", "Subtract", "Multiply", "Divide"]
tk.OptionMenu(root, operation_var, *operations).pack()

tk.Button(root, text="Calculate", command=calculate).pack()
result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()
