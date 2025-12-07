import tkinter as tk
from tkinter import ttk
import math

class CalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator | Developed by Noor Faisel")
        self.root.geometry("420x620")
        self.root.resizable(False, False)

        self.expression = ""
        self.create_widgets()
        self.setup_keyboard_bindings()

    # ---------------------- UI SETUP ----------------------
    def create_widgets(self):
        self.display = tk.Entry(self.root, font=("Segoe UI", 28), justify="right", bd=0, bg="#1E1E1E", fg="white")
        self.display.pack(fill="both", padx=30, pady=30, ipady=30)

        btn_frame = tk.Frame(self.root, bg="black")
        btn_frame.pack(expand=True, fill="both")

        buttons = [
            ["C", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", "√"],
        ]

        for row in buttons:
            row_frame = tk.Frame(btn_frame, bg="black")
            row_frame.pack(expand=True, fill="both")

            for btn_text in row:
                button = tk.Button(
                    row_frame, text=btn_text, font=("Segoe UI", 22), fg="white",
                    bg="#4D1F1F" if btn_text not in ["C", "=", "√"] else ("#1ACBFC" if btn_text == "C" else "#42F011"),
                    bd=0, relief="flat", activebackground="#38585F",
                    command=lambda txt=btn_text: self.handle_button(txt)
                )
                button.pack(side="left", expand=True, fill="both", padx=3, pady=3)

    # ---------------------- BUTTON HANDLING ----------------------
    def handle_button(self, txt):
        if txt == "C":
            self.clear()
        elif txt == "⌫":
            self.backspace()
        elif txt == "=":
            self.calculate()
        elif txt == "√":
            self.square_root()
        else:
            self.input_char(txt)

    def input_char(self, char):
        self.expression += char
        self.update_display()

    def input_digit(self, digit):
        self.expression += digit
        self.update_display()

    def input_operator(self, op):
        self.expression += op
        self.update_display()

    def input_decimal(self):
        self.expression += "."
        self.update_display()

    def clear(self):
        self.expression = ""
        self.update_display()

    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_display()

    def square_root(self):
        try:
            result = math.sqrt(float(self.expression))
            self.expression = str(result)
            self.update_display()
        except:
            self.display_error()

    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.update_display()
        except:
            self.display_error()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def display_error(self):
        self.expression = "Error"
        self.update_display()

    # ---------------------- KEYBOARD SUPPORT ----------------------
    def setup_keyboard_bindings(self):

        # Digits top row + numpad
        for i in range(10):
            self.root.bind(str(i), lambda e, num=str(i): self.input_digit(num))
            self.root.bind(f'<KP_{i}>', lambda e, num=str(i): self.input_digit(num))

        # Operators
        ops = {"+": "+", "-": "-", "*": "*", "/": "/"}
        for key, op in ops.items():
            self.root.bind(key, lambda e, o=op: self.input_operator(o))

        # Numpad operators
        self.root.bind("<KP_Add>", lambda e: self.input_operator("+"))
        self.root.bind("<KP_Subtract>", lambda e: self.input_operator("-"))
        self.root.bind("<KP_Multiply>", lambda e: self.input_operator("*"))
        self.root.bind("<KP_Divide>", lambda e: self.input_operator("/"))

        # Decimal
        self.root.bind(".", lambda e: self.input_decimal())
        self.root.bind("<KP_Decimal>", lambda e: self.input_decimal())

        # Enter/Equals
        self.root.bind("<Return>", lambda e: self.calculate())
        self.root.bind("=", lambda e: self.calculate())
        self.root.bind("<KP_Enter>", lambda e: self.calculate())

        # Clear
        self.root.bind("<Escape>", lambda e: self.clear())

        # Backspace
        self.root.bind("<BackSpace>", lambda e: self.backspace())

# ---------------------- MAIN ----------------------
def main():
    root = tk.Tk()
    CalculatorUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
