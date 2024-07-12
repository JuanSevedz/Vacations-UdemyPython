import tkinter as tk


class Calculator(tk.Tk):
    """A simple calculator application using Tkinter."""

    def __init__(self):
        """Initialize the Calculator."""
        super().__init__()
        self.geometry("520x480")
        self.resizable(0, 0)
        self.title("Calculator")
        
        # Class attributes
        self.expression = ""
        self.entry = None  # Text box (input)
        self.entry_text = tk.StringVar()  # StringVar to get input value
        self._create_components()  # Create GUI components

    def _create_components(self):
        """Create GUI components for the calculator."""
        # Frame for text box
        entry_frame = tk.Frame(self, width=400, height=50, bg="grey")
        entry_frame.pack(side=tk.TOP)

        # Text Box
        self.entry = tk.Entry(
            entry_frame,
            font=("Arial", 18, "bold"),
            textvariable=self.entry_text,
            width=30,
            justify=tk.RIGHT,
        )
        self.entry.grid(row=0, column=0, ipady=10)

        # Frame for buttons
        buttons_frame = tk.Frame(self, width=400, height=450, bg="grey")
        buttons_frame.pack()

        # First row
        # Clear Button
        clear_button = tk.Button(
            buttons_frame,
            text="C",
            width="32",
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=self._clear_event,
        )
        clear_button.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        # Divide Button
        divide_button = tk.Button(
            buttons_frame,
            text="/",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self._click_event("/"),
        )
        divide_button.grid(row=0, column=3, padx=1, pady=1)

        # Second row
        seven_button = tk.Button(
            buttons_frame,
            text="7",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._click_event(7),
        )
        seven_button.grid(row=1, column=0, padx=1, pady=1)

        eight_button = tk.Button(
            buttons_frame,
            text="8",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._click_event(8),
        )
        eight_button.grid(row=1, column=1, padx=1, pady=1)

        nine_button = tk.Button(
            buttons_frame,
            text="9",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._click_event(9),
        )
        nine_button.grid(row=1, column=2, padx=1, pady=1)

        multiply_button = tk.Button(
            buttons_frame,
            text="*",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self._click_event("*"),
        )
        multiply_button.grid(row=1, column=3, padx=1, pady=1)

        # Third row
        four_button = tk.Button(
            buttons_frame,
            text="4",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._click_event(4),
        )
        four_button.grid(row=2, column=0, padx=1, pady=1)

        five_button = tk.Button(
            buttons_frame,
            text="5",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._click_event(5),
        )
        five_button.grid(row=2, column=1, padx=1, pady=1)

        six_button = tk.Button(
            buttons_frame,
            text="6",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._click_event(6),
        )
        six_button.grid(row=2, column=2, padx=1, pady=1)

        subtract_button = tk.Button(
            buttons_frame,
            text="-",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self._click_event("-"),
        )
        subtract_button.grid(row=2, column=3, padx=1, pady=1)

        # Fourth row
        one_button = tk.Button(
            buttons_frame,
            text="1",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._click_event(1),
        )
        one_button.grid(row=3, column=0, padx=1, pady=1)

        two_button = tk.Button(
            buttons_frame,
            text="2",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._click_event(2),
        )
        two_button.grid(row=3, column=1, padx=1, pady=1)

        three_button = tk.Button(
            buttons_frame,
            text="3",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._click_event(3),
        )
        three_button.grid(row=3, column=2, padx=1, pady=1)

        add_button = tk.Button(
            buttons_frame,
            text="+",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self._click_event("+"),
        )
        add_button.grid(row=3, column=3, padx=1, pady=1)

        # Fifth row
        zero_button = tk.Button(
            buttons_frame,
            text="0",
            width=21,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._click_event(0),
        )
        zero_button.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

        decimal_button = tk.Button(
            buttons_frame,
            text=".",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self._click_event("."),
        )
        decimal_button.grid(row=4, column=2, padx=1, pady=1)

        equal_button = tk.Button(
            buttons_frame,
            text="=",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=self._evaluate_event,
        )
        equal_button.grid(row=4, column=3, padx=1, pady=1)

    def _evaluate_event(self):
        """Evaluate the arithmetic expression."""
        result = str(eval(self.expression))
        self.entry_text.set(result)
        self.expression = ""

    def _clear_event(self):
        """Clear the expression."""
        self.expression = ""
        self.entry_text.set(self.expression)

    def _click_event(self, element):
        """Concatenate the new element to the existing expression."""
        self.expression = f"{self.expression}{element}"
        self.entry_text.set(self.expression)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
