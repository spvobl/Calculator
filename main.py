import tkinter as tk


class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Simple Calculator')
        self.entry = tk.Entry(self, width=40, borderwidth=5)
        self.buttons = []
        self.buttons = [tk.Button(self, text=str(i), padx=40, pady=20, command=lambda i=i: self.button_click(i)) for i
                        in range(10)]
        self.button_plus = tk.Button(self, text="+", padx=39, pady=20, command=self.button_add)
        self.buttons_equal = tk.Button(self, text="=", padx=87, pady=20, command=self.button_sum)
        self.button_clear = tk.Button(self, text="clear", padx=78, pady=20, command=self.button_clear)
        self.create_widgets()
        self.grid()
        self.curr = ""
        self.result = False

    def create_widgets(self):
        self.entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        j = 4
        for i in range(1, 10):
            if i % 3 == 1:
                j -= 1
            self.buttons[i].grid(row=j, column=(i - 1) % 3)

        self.buttons[0].grid(row=4, column=0)
        self.button_clear.grid(row=4, column=1, columnspan=2)
        self.button_plus.grid(row=5, column=0)
        self.buttons_equal.grid(row=5, column=1, columnspan=2)

    def button_click(self, number):
        if self.result:
            self.entry.delete(0, 'end')
            self.result = False
        current = self.entry.get()
        self.entry.delete(0, 'end')
        self.entry.insert(0, str(current) + str(number))

    def button_add(self):
        if self.curr:
            self.button_sum()
            self.curr = self.entry.get()
        else:
            self.curr = self.entry.get()
            self.entry.delete(0, 'end')

    def button_sum(self):
        current = self.entry.get()
        self.entry.delete(0, 'end')
        self.entry.insert(0, int(self.curr) + int(current))
        self.curr = ""
        self.result = True

    def button_clear(self):
        self.entry.delete(0, 'end')


if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(master=root)
    calculator.mainloop()
