import tkinter as tk
from tkinter import ttk

# App window
root = tk.Tk()
root.title("CALCULATOR")
root.geometry("360x500")
root.resizable(False, False)
root.configure(bg="#1c1c1c")

# Style
style = ttk.Style()
style.theme_use("clam")

# Display Frame
display_frame = tk.Frame(root, bg="#1c1c1c")
display_frame.pack(expand=True, fill="both")

equation = tk.StringVar()
entry = tk.Entry(display_frame, textvariable=equation, font=("Helvetica", 28),
                 bg="#1c1c1c", fg="#ffffff", bd=0, insertbackground="white", justify="right")
entry.pack(expand=True, fill="both", ipady=20)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#1c1c1c")
btn_frame.pack(expand=True, fill="both")

# Buttons text layout
buttons = [
    ("C", 1, 0), ("%", 1, 1), ("←", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2)
]

def click(event):
    text = event.widget["text"]

    if text == "=":
        try:
            result = eval(equation.get())
            equation.set(result)
        except:
            equation.set("Error")
    elif text == "C":
        equation.set("")
    elif text == "←":
        equation.set(equation.get()[:-1])
    else:
        equation.set(equation.get() + text)

# Create Buttons
for (text, row, col) in buttons:
    btn = tk.Button(
        btn_frame, text=text,
        font=("Helvetica", 20),
        fg="white",
        bg="#333333" if text not in ("=", "+", "-", "*", "/") else "#ff8c00",
        activebackground="#666666",
        activeforeground="white",
        relief="flat",
        borderwidth=0
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
    btn.bind("<Button-1>", click)

# Adjust grid weights
for i in range(6):
    btn_frame.rowconfigure(i, weight=1)
for i in range(4):
    btn_frame.columnconfigure(i, weight=1)

root.mainloop()
