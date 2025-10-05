import tkinter as tk
from tkinter import ttk
import math

#CALCULATOR APP# 
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator (shiv)")
        self.geometry("350x500")
        self.minsize(300, 450)
        self.configure(bg="#222")

        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        # Entry box (display)
        self.display_var = tk.StringVar()
        entry = ttk.Entry(
            self,
            textvariable=self.display_var,
            font=("Segoe UI", 22),
            justify="right"
        )
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=15)
        entry.configure(state="readonly")

        # Button layout
        buttons = [
            ("C", 1, 0, "#ff6666"), ("←", 1, 1, "#ffb366"), ("%", 1, 2, "#4da6ff"), ("/", 1, 3, "#4da6ff"),
            ("7", 2, 0, "#333"), ("8", 2, 1, "#333"), ("9", 2, 2, "#333"), ("*", 2, 3, "#4da6ff"),
            ("4", 3, 0, "#333"), ("5", 3, 1, "#333"), ("6", 3, 2, "#333"), ("-", 3, 3, "#4da6ff"),
            ("1", 4, 0, "#333"), ("2", 4, 1, "#333"), ("3", 4, 2, "#333"), ("+", 4, 3, "#4da6ff"),
            ("0", 5, 0, "#333"), (".", 5, 1, "#333"), ("x²", 5, 2, "#4da6ff"), ("x³", 5, 3, "#4da6ff"),
            ("=", 6, 0, "#00b33c", 4)
        ]

        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            color = btn[3]
            colspan = btn[4] if len(btn) > 4 else 1

            b = tk.Button(
                self,
                text=text,
                font=("Segoe UI", 18, "bold"),
                bg=color,
                fg="white",
                bd=0,
                relief="ridge",
                activebackground="#666",
                command=lambda val=text: self.on_button_click(val)
            )
            b.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

        # Make grid responsive
        for i in range(7):
            self.rowconfigure(i, weight=1)
        for j in range(4):
            self.columnconfigure(j, weight=1)

    def on_button_click(self, value):
        if value == "C":
            self.expression = ""
        elif value == "←":
            self.expression = self.expression[:-1]
        elif value == "=":
            self.calculate()
        elif value == "x²":
            self.square()
        elif value == "x³":
            self.cube()
        elif value == "%":
            self.percent()
        else:
            self.expression += value
        self.display_var.set(self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
        except Exception:
            self.expression = "Error"
        self.display_var.set(self.expression)

    def square(self):
        try:
            value = float(self.expression)
            result = value ** 2
            self.expression = str(result)
            self.display_var.set(self.expression)
        except Exception:
            self.expression = "Error"
            self.display_var.set(self.expression)

    def cube(self):
        try:
            value = float(self.expression)
            result = value ** 3
            self.expression = str(result)
            self.display_var.set(self.expression)
        except Exception:
            self.expression = "Error"
            self.display_var.set(self.expression)

    def percent(self):
        try:
            value = float(self.expression)
            result = value / 100
            self.expression = str(result)
            self.display_var.set(self.expression)
        except Exception:
            self.expression = "Error"
            self.display_var.set(self.expression)


#RUN APP#
if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
