"""
gui.py

Main graphical user interface for the Scientific Calculator.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

from calculator import Calculator
from scientific import Scientific
from matrix import Matrix
from equations import EquationSolver
from statistics_module import Statistics
from conversions import Converter
from history import HistoryManager
from memory import Memory
from themes import ThemeManager
from utils import format_number


class ScientificCalculatorApp(tk.Tk):

    def __init__(self):
        super().__init__()

        # -------------------------
        # Window
        # -------------------------

        self.title("Scientific Calculator")
        self.geometry("700x700")
        self.minsize(650, 650)
        self.resizable(True, True)

        self.expression = ""

        self.memory = Memory()
        self.history = HistoryManager()
        self.theme = ThemeManager()

        self.configure(bg=self.theme.current()["bg"])

        # -------------------------
        # Build GUI
        # -------------------------

        self.create_menu()

        self.create_display()

        self.create_history()

        self.create_button_frame()

        self.create_buttons()

        self.bind_keyboard()
    # ==========================================================
    # MENU BAR
    # ==========================================================

    def create_menu(self):

        menubar = tk.Menu(self)

        # ---------- File ----------

        file_menu = tk.Menu(
            menubar,
            tearoff=0
        )

        file_menu.add_command(
            label="Save History",
            command=self.save_history
        )

        file_menu.add_command(
            label="Clear History",
            command=self.clear_history
        )

        file_menu.add_separator()

        file_menu.add_command(
            label="Exit",
            command=self.destroy
        )

        menubar.add_cascade(
            label="File",
            menu=file_menu
        )

        # ---------- View ----------

        view_menu = tk.Menu(
            menubar,
            tearoff=0
        )

        view_menu.add_command(
            label="Light Theme",
            command=self.set_light_theme
        )

        view_menu.add_command(
            label="Dark Theme",
            command=self.set_dark_theme
        )

        menubar.add_cascade(
            label="View",
            menu=view_menu
        )

        # ---------- Tools ----------

        tools_menu = tk.Menu(
            menubar,
            tearoff=0
        )

        tools_menu.add_command(
            label="Matrix Calculator",
            command=self.open_matrix_window
        )

        tools_menu.add_command(
            label="Statistics",
            command=self.open_statistics_window
        )

        tools_menu.add_command(
            label="Unit Converter",
            command=self.open_converter_window
        )

        tools_menu.add_command(
            label="Equation Solver",
            command=self.open_equation_window
        )

        menubar.add_cascade(
            label="Tools",
            menu=tools_menu
        )

        # ---------- Help ----------

        help_menu = tk.Menu(
            menubar,
            tearoff=0
        )

        help_menu.add_command(
            label="About",
            command=self.about
        )

        menubar.add_cascade(
            label="Help",
            menu=help_menu
        )

        self.config(menu=menubar)

    # ==========================================================
    # DISPLAY
    # ==========================================================

    def create_display(self):

        theme = self.theme.current()

        self.display = tk.Entry(
            self,
            font=("Segoe UI", 24),
            justify="right",
            bd=6,
            relief=tk.GROOVE,
            bg=theme["display_bg"],
            fg=theme["display_fg"]
        )

        self.display.pack(
            fill="x",
            padx=10,
            pady=10
        )

    # ==========================================================
    # HISTORY
    # ==========================================================

    def create_history(self):

        frame = tk.LabelFrame(
            self,
            text="History",
            padx=5,
            pady=5
        )

        frame.pack(
            fill="x",
            padx=10
        )

        self.history_box = tk.Text(
            frame,
            height=7,
            font=("Consolas", 10),
            state="disabled"
        )

        self.history_box.pack(
            fill="x"
        )

    def add_history(self, expression, result):

        self.history.add(expression, result)

        self.history_box.configure(
            state="normal"
        )

        self.history_box.insert(
            tk.END,
            f"{expression} = {result}\n"
        )

        self.history_box.configure(
            state="disabled"
        )

        self.history_box.see(
            tk.END
        )

    def save_history(self):

        self.history.save()

        messagebox.showinfo(
            "Saved",
            "History saved successfully."
        )

    def clear_history(self):

        self.history.clear()

        self.history_box.configure(
            state="normal"
        )

        self.history_box.delete(
            "1.0",
            tk.END
        )

        self.history_box.configure(
            state="disabled"
        )

    # ==========================================================
    # BUTTON FRAME
    # ==========================================================

    def create_button_frame(self):

        self.button_frame = tk.Frame(self)

        self.button_frame.pack(
            expand=True,
            fill="both",
            padx=10,
            pady=10
        )

    # ==========================================================
    # KEYBOARD
    # ==========================================================

    def bind_keyboard(self):

        self.bind(
            "<Return>",
            lambda e: self.equal()
        )

        self.bind(
            "<BackSpace>",
            lambda e: self.delete()
        )

        self.bind(
            "<Escape>",
            lambda e: self.clear()
        )

        for key in "0123456789+-*/().":

            self.bind(
                key,
                lambda e,
                k=key: self.press(k)
            )

    # ==========================================================
    # BUTTONS
    # ==========================================================

    def create_buttons(self):

        buttons = [

            ["MC", "MR", "MS", "M+", "M-"],

            ["sin", "cos", "tan", "log", "ln"],

            ["√", "x²", "xʸ", "π", "e"],

            ["7", "8", "9", "/", "DEL"],

            ["4", "5", "6", "*", "C"],

            ["1", "2", "3", "-", "("],

            ["0", ".", "=", "+", ")"]

        ]

        colors = {

            "number": "#FFFFFF",

            "operator": "#E8F0FE",

            "scientific": "#FFF3CD",

            "memory": "#D1ECF1",

            "equal": "#4CAF50"

        }

        for row in buttons:

            row_frame = tk.Frame(
                self.button_frame
            )

            row_frame.pack(
                fill="both",
                expand=True
            )

            for text in row:

                if text in [
                    "MC",
                    "MR",
                    "MS",
                    "M+",
                    "M-"
                ]:

                    bg = colors["memory"]

                elif text in [
                    "sin",
                    "cos",
                    "tan",
                    "log",
                    "ln",
                    "√",
                    "x²",
                    "xʸ",
                    "π",
                    "e"
                ]:

                    bg = colors["scientific"]

                elif text == "=":

                    bg = colors["equal"]

                elif text in [
                    "+",
                    "-",
                    "*",
                    "/",
                    "(",
                    ")",
                    "DEL",
                    "C"
                ]:

                    bg = colors["operator"]

                else:

                    bg = colors["number"]

                button = tk.Button(

                    row_frame,

                    text=text,

                    font=("Segoe UI", 15, "bold"),

                    relief=tk.RAISED,

                    bd=1,

                    bg=bg,

                    activebackground="#B8D7FF",

                    command=lambda value=text:
                    self.button_action(value)

                )

                button.pack(

                    side="left",

                    expand=True,

                    fill="both",

                    padx=2,

                    pady=2

                )

    # ==========================================================
    # DISPLAY FUNCTIONS
    # ==========================================================

    def press(self, value):

        self.expression += str(value)

        self.display.delete(0, tk.END)

        self.display.insert(

            tk.END,

            self.expression

        )

    def clear(self):

        self.expression = ""

        self.display.delete(

            0,

            tk.END

        )

    def delete(self):

        self.expression = self.expression[:-1]

        self.display.delete(

            0,

            tk.END

        )

        self.display.insert(

            tk.END,

            self.expression

        )

    # ==========================================================
    # MEMORY FUNCTIONS
    # ==========================================================

    def memory_clear(self):

        self.memory.clear()

    def memory_store(self):

        try:

            value = float(

                self.display.get()

            )

            self.memory.store(

                value

            )

        except:

            pass

    def memory_recall(self):

        value = self.memory.recall()

        self.expression = str(value)

        self.display.delete(

            0,

            tk.END

        )

        self.display.insert(

            tk.END,

            value

        )

    def memory_add(self):

        try:

            self.memory.add(

                float(

                    self.display.get()

                )

            )

        except:

            pass

    def memory_subtract(self):

        try:

            self.memory.subtract(

                float(

                    self.display.get()

                )

            )

        except:

            pass

    # ==========================================================
    # CALCULATE
    # ==========================================================

    def equal(self):

        try:

            expression = self.expression.replace("^", "**")

            result = eval(expression)

            result = format_number(result)

            self.display.delete(0, tk.END)

            self.display.insert(tk.END, result)

            self.add_history(self.expression, result)

            self.expression = str(result)

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Invalid Expression\n\n{e}"
            )

            self.clear()

    # ==========================================================
    # BUTTON ACTIONS
    # ==========================================================

    def button_action(self, text):

        try:

            # ==========================
            # BASIC
            # ==========================

            if text == "=":
                self.equal()

            elif text == "C":
                self.clear()

            elif text == "DEL":
                self.delete()

            # ==========================
            # MEMORY
            # ==========================

            elif text == "MC":
                self.memory_clear()

            elif text == "MR":
                self.memory_recall()

            elif text == "MS":
                self.memory_store()

            elif text == "M+":
                self.memory_add()

            elif text == "M-":
                self.memory_subtract()

            # ==========================
            # CONSTANTS
            # ==========================

            elif text == "π":

                self.press(str(Scientific.pi()))

            elif text == "e":

                self.press(str(Scientific.e()))

            # ==========================
            # SQUARE ROOT
            # ==========================

            elif text == "√":

                value = float(self.display.get())

                answer = Calculator.square_root(value)

                answer = format_number(answer)

                self.display.delete(0, tk.END)

                self.display.insert(tk.END, answer)

                self.add_history(
                    f"√({value})",
                    answer
                )

                self.expression = str(answer)

            # ==========================
            # SQUARE
            # ==========================

            elif text == "x²":

                value = float(self.display.get())

                answer = Calculator.square(value)

                answer = format_number(answer)

                self.display.delete(0, tk.END)

                self.display.insert(tk.END, answer)

                self.add_history(
                    f"{value}²",
                    answer
                )

                self.expression = str(answer)

            # ==========================
            # POWER
            # ==========================

            elif text == "xʸ":

                self.press("**")

            # ==========================
            # SIN
            # ==========================

            elif text == "sin":

                value = float(self.display.get())

                answer = Scientific.sin(value)

                answer = format_number(answer)

                self.display.delete(0, tk.END)

                self.display.insert(tk.END, answer)

                self.add_history(
                    f"sin({value})",
                    answer
                )

                self.expression = str(answer)

            # ==========================
            # COS
            # ==========================

            elif text == "cos":

                value = float(self.display.get())

                answer = Scientific.cos(value)

                answer = format_number(answer)

                self.display.delete(0, tk.END)

                self.display.insert(tk.END, answer)

                self.add_history(
                    f"cos({value})",
                    answer
                )

                self.expression = str(answer)

            # ==========================
            # TAN
            # ==========================

            elif text == "tan":

                value = float(self.display.get())

                answer = Scientific.tan(value)

                answer = format_number(answer)

                self.display.delete(0, tk.END)

                self.display.insert(tk.END, answer)

                self.add_history(
                    f"tan({value})",
                    answer
                )

                self.expression = str(answer)

            # ==========================
            # LOG
            # ==========================

            elif text == "log":

                value = float(self.display.get())

                answer = Scientific.log(value)

                answer = format_number(answer)

                self.display.delete(0, tk.END)

                self.display.insert(tk.END, answer)

                self.add_history(
                    f"log({value})",
                    answer
                )

                self.expression = str(answer)

            # ==========================
            # LN
            # ==========================

            elif text == "ln":

                value = float(self.display.get())

                answer = Scientific.ln(value)

                answer = format_number(answer)

                self.display.delete(0, tk.END)

                self.display.insert(tk.END, answer)

                self.add_history(
                    f"ln({value})",
                    answer
                )

                self.expression = str(answer)

            # ==========================
            # EVERYTHING ELSE
            # ==========================

            else:

                self.press(text)

        except Exception as e:

            messagebox.showerror(
                "Calculator Error",
                str(e)
            )

    # ==========================================================
    # MATRIX WINDOW
    # ==========================================================

    def open_matrix_window(self):

        messagebox.showinfo(
            "Matrix Calculator",
            "Matrix Calculator GUI\n"
            "Coming in Version 2.\n\n"
            "The Matrix class is already implemented."
        )

    # ==========================================================
    # STATISTICS WINDOW
    # ==========================================================

    def open_statistics_window(self):

        data = simpledialog.askstring(
            "Statistics",
            "Enter numbers separated by commas:"
        )

        if not data:
            return

        try:

            numbers = [float(i.strip()) for i in data.split(",")]

            result = (
                f"Mean : {Statistics.mean(numbers)}\n"
                f"Median : {Statistics.median(numbers)}\n"
                f"Mode : {Statistics.mode(numbers)}\n"
                f"Std Dev : {Statistics.standard_deviation(numbers)}"
            )

            messagebox.showinfo(
                "Statistics Result",
                result
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==========================================================
    # CONVERTER
    # ==========================================================

    def open_converter_window(self):

        messagebox.showinfo(
            "Converter",
            "Converter GUI\n"
            "Coming in Version 2.\n\n"
            "All conversion functions are already implemented."
        )

    # ==========================================================
    # EQUATION SOLVER
    # ==========================================================

    def open_equation_window(self):

        try:

            a = float(simpledialog.askstring("Equation", "Enter a"))
            b = float(simpledialog.askstring("Equation", "Enter b"))
            c = float(simpledialog.askstring("Equation", "Enter c"))

            result = EquationSolver.solve_quadratic(a, b, c)

            messagebox.showinfo(
                "Solution",
                str(result)
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==========================================================
    # THEMES
    # ==========================================================

    def set_dark_theme(self):

        self.theme.dark()

        t = self.theme.current()

        self.configure(bg=t["bg"])

        self.display.configure(
            bg=t["display_bg"],
            fg=t["display_fg"]
        )

    def set_light_theme(self):

        self.theme.light()

        t = self.theme.current()

        self.configure(bg=t["bg"])

        self.display.configure(
            bg=t["display_bg"],
            fg=t["display_fg"]
        )

    # ==========================================================
    # ABOUT
    # ==========================================================

    def about(self):

        messagebox.showinfo(

            "About",

            "Scientific Calculator\n\n"

            "Version 1.0\n\n"

            "Developed in Python using Tkinter.\n\n"

            "Features:\n"

            "• Scientific Calculator\n"

            "• Matrix Operations\n"

            "• Statistics\n"

            "• Equation Solver\n"

            "• Unit Converter\n"

            "• History\n"

            "• Memory\n"

            "• Dark / Light Theme"

        )


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    app = ScientificCalculatorApp()

    app.mainloop()