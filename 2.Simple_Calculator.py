# To design a simple calculator with basic arithmetic operations using python.

import tkinter as tk

calculator_width = 400
calculator_height = 500

# Function to perform arithematic operations-

def perform_calculation():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()
    
    if operation == '+':
        result.set(num1 + num2)
    elif operation == '-':
        result.set(num1 - num2)
    elif operation == '*':
        result.set(num1 * num2)
    elif operation == '/':
        if num2 != 0:
            result.set(num1 / num2)
        else:
            result.set("Error: Division by zero")
    else:
        result.set("Error: Invalid operation")

# To create the main window-

Calculator = tk.Tk()
Calculator.title("Simple Calculator")
Calculator.geometry(f"{calculator_width}x{calculator_height}")

# To create input fields-

# To create a label for first number input-

label_num1 = tk.Label(Calculator, text="Enter the first number:", width=40, font=10)
label_num1.pack(pady=10)

# To create an entry field for first number length-

entry_num1 = tk.Entry(Calculator, width=30, font=8)
entry_num1.pack(pady=10)

# To create a label for second number input-

label_num2 = tk.Label(Calculator, text="Enter the second number:", width=20, font=10)
label_num2.pack(pady=10)

# To create an entry field for second number length-

entry_num2 = tk.Entry(Calculator, width=30, font=8)
entry_num2.pack(pady=10)

# To create operation choice-

operation_var = tk.StringVar()
operation_var.set('+')  # Default operation
label_operation = tk.Label(Calculator, text="Choose an operation:", width=30, font=10)
label_operation.pack(pady=10)
operations = ["+", "-", "*", "/"]
operation_menu = tk.OptionMenu(Calculator, operation_var, *operations)
operation_menu.pack(pady=10)

# To create the Calculate button-

calculate_button = tk.Button(Calculator, text="Calculate", command=perform_calculation, width=20, font=10)
calculate_button.pack(pady=10)

# To create a label to display the result-

result = tk.StringVar()
result.set("Result will be displayed here")
result_label = tk.Label(Calculator, textvariable=result, width=30, font=10)
result_label.pack(pady=10)

# Main loop-

Calculator.mainloop()
