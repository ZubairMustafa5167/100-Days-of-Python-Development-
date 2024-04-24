import tkinter as tk

def click1(number):
    entry.insert(tk.END, str(number))

def click_dot():
    entry.insert(tk.END, ".")

def click_operation(operation):
    entry.insert(tk.END, operation)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
mf = tk.Frame(root)

# Entry widget for input
entry = tk.Entry(mf, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Number buttons
buttons = []
for i in range(10):
    buttons.append(tk.Button(mf, text=str(i), fg='green', command=lambda i=i: click1(i)))
    
buttons[1].grid(row=3, column=0)
buttons[2].grid(row=3, column=1)
buttons[3].grid(row=3, column=2)
buttons[4].grid(row=2, column=0)
buttons[5].grid(row=2, column=1)
buttons[6].grid(row=2, column=2)
buttons[7].grid(row=1, column=0)
buttons[8].grid(row=1, column=1)
buttons[9].grid(row=1, column=2)
buttons[0].grid(row=4, column=0)

# Dot button
dot = tk.Button(mf, text='.', fg='green', command=click_dot)
dot.grid(row=4, column=1)

# Operations buttons
plus = tk.Button(mf, text='+', fg='green', command=lambda: click_operation("+"))
minus = tk.Button(mf, text='-', fg='green', command=lambda: click_operation("-"))
multip = tk.Button(mf, text='x', fg='green', command=lambda: click_operation("*"))
divid = tk.Button(mf, text='/', fg='green', command=lambda: click_operation("/"))
equal = tk.Button(mf, text='=', fg='green', command=calculate)

plus.grid(row=1, column=3)
minus.grid(row=2, column=3)
multip.grid(row=3, column=3)
divid.grid(row=4, column=3)
equal.grid(row=4, column=2)

mf.pack()

root.mainloop()

