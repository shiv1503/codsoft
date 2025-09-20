import tkinter as tk
from tkinter import messagebox

# Function to handle the math operations
def do_calculation():
    """
    Reads numbers from the entry fields and performs the selected operation.
    Displays the result or an error message.
    """
    try:
        first_num = float(first_entry.get())
        second_num = float(second_entry.get())
        chosen_op = op_choice.get()

        # Perform the selected operation
        if chosen_op == '+':
            answer = first_num + second_num
        elif chosen_op == '-':
            answer = first_num - second_num
        elif chosen_op == '*':
            answer = first_num * second_num
        elif chosen_op == '/':
            if second_num == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero!")
                return
            answer = first_num / second_num
        else:
            messagebox.showerror("Operation Error", "Unknown operation selected.")
            return

        # Show the result
        result_text.config(text=f"Result: {answer}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# ------------------ UI Section ------------------ #
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("360x220")  # a slightly bigger window

# First number
tk.Label(window, text="First Number:").pack(pady=3)
first_entry = tk.Entry(window)
first_entry.pack()

# Second number
tk.Label(window, text="Second Number:").pack(pady=3)
second_entry = tk.Entry(window)
second_entry.pack()

# Operation selection
tk.Label(window, text="Choose an operation:").pack(pady=3)
op_choice = tk.StringVar(value='+')  # default operation

# Frame for radio buttons
ops_frame = tk.Frame(window)
ops_frame.pack()

# Use simpler labels for clarity
tk.Radiobutton(ops_frame, text="Add (+)", variable=op_choice, value='+').pack(side=tk.LEFT, padx=5)
tk.Radiobutton(ops_frame, text="Subtract (-)", variable=op_choice, value='-').pack(side=tk.LEFT, padx=5)
tk.Radiobutton(ops_frame, text="Multiply (*)", variable=op_choice, value='*').pack(side=tk.LEFT, padx=5)
tk.Radiobutton(ops_frame, text="Divide (/)", variable=op_choice, value='/').pack(side=tk.LEFT, padx=5)

# Calculate button
tk.Button(window, text="Calculate", command=do_calculation).pack(pady=8)

# Result display
result_text = tk.Label(window, text="Result: ")
result_text.pack(pady=5)

window.mainloop()
