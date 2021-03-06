import tkinter as tk


class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Simple Calculator')
        self.master.resizable(0, 0)
        self.entry = tk.Entry(self, width=30, borderwidth=5)
        self.buttons = []
        self.buttons = [tk.Button(self, text=str(i), width=10, height=5, command=lambda i=i: self.button_click(i)) for i in range(10)]
        self.buttons[0] = tk.Button(self,text="0", width=20, height=5, command=lambda:self.button_click(0))
        self.button_plus = tk.Button(self, text="+", width=10, height=5, command= lambda: self.button_op("+"))
        self.button_minus = tk.Button(self, text="-", width=10, height=5, command=lambda: self.button_op("-"))
        self.button_div = tk.Button(self, text="÷", width=10, height=5, command=lambda: self.button_op("/"))
        self.button_multi = tk.Button(self, text="X", width=10, height=5, command=lambda: self.button_op("*"))
        self.button_equal = tk.Button(self, text="=", width=10, height=5, command=lambda: self.button_eval(self.operation))
        self.button_clear = tk.Button(self, text="C", width=10, height=5, command=self.button_clear)
        self.button_minsym = tk.Button(self, text="+/-", width=10, height=5, command=self.button_negative)
        self.button_percent = tk.Button(self,text="%", width=10, height=5, command=self.button_percentage)
        self.button_decimal = tk.Button(self,text=".", width=10, height=5, command=self.button_point)
        self.create_widgets()
        self.grid()
        self.curr = ""
        self.result = False
        self.operation = ""
        self.firstNum = ""

    def create_widgets(self):
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        j = 5
        for i in range(1, 10):
            if i % 3 == 1:
                j -= 1
            self.buttons[i].grid(row=j, column=(i - 1) % 3)

        self.buttons[0].grid(row=5, column=0, columnspan=2)
        self.button_clear.grid(row=1, column=0)
        self.button_plus.grid(row=4, column=3)
        self.button_equal.grid(row=5, column=3)
        self.button_multi.grid(row=2, column=3)
        self.button_minus.grid(row=3, column=3)
        self.button_div.grid(row=1, column=3)
        self.button_minsym.grid(row=1,column=1)
        self.button_percent.grid(row=1,column=2)
        self.button_decimal.grid(row=5,column=2)

    def button_percentage(self):
        current = self.entry.get()
        if current != "Error":
            self.entry.delete(0,'end')
            self.entry.insert(0, str(float(current)/100))

        
    def button_negative(self):
        current = self.entry.get()
        if current != "Error" and current != "0":
            self.entry.delete(-1, 'end')
            if "-" in current:
                self.entry.insert(-1,current[1:])
            else:
                self.entry.insert(-1,"-"+ current)


        
    def button_point(self):
        current = self.entry.get()
        if "." not in current and current != "Error":
            self.entry.delete(0, "end")
            self.entry.insert(0,current+".")

    def button_click(self, number):
        if self.result:
            self.entry.delete(0, 'end')
            self.result = False
        if self.firstNum:
            self.entry.delete(0,'end')
            self.firstNum = ""
        current = self.entry.get()
        self.entry.delete(0, 'end')
        self.entry.insert(0, str(current) + str(number))

    def button_eval(self, op):
        try:  
            current = self.entry.get()
            self.entry.delete(0, 'end')
            self.entry.insert(0, eval(self.curr +op+  current))
            self.curr = ""
            self.result = True
        except:
            self.entry.delete(0,'end')
            self.entry.insert(0, 'Error')
            self.curr = ""
            self.result = True

    def button_op(self, op):
        selfBool = bool(self.operation)
        self.operation = op
        if self.curr and self.firstNum != op:
            self.firstNum = op
            self.button_eval(op)
            self.curr = self.entry.get()
        else:
            self.curr = self.entry.get()
            self.firstNum = op
           # self.entry.delete(0, "end")

    def button_clear(self):
        self.entry.delete(0, 'end')
        self.curr = ""
        self.result = False
        self.firtNum = ""


if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(master=root)
    calculator.mainloop()
