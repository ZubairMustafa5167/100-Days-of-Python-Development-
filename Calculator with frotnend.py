from tkinter import *

myroot=Tk()
myroot.geometry('1000x1000')
myroot.configure(bg="white")
myroot.title('Calculator')
mf=Frame(myroot,width=700,height=700,bg='cyan')
mf.propagate(0)
mf.pack()
         

entry =Entry(mf, width=20)
entry.place(x=100, y=100)
         
def click1(number):
    entry.insert(END, str(number))

def click_dot():
    entry.insert(END, ".")

def click_operation(operation):
    entry.insert(END, operation)
         
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Number Button
first=Button(mf,text='1',fg='green',command= lambda: click1(1))
second=Button(mf,text='2',fg='green',command= lambda: click1(2))
third=Button(mf,text='3',fg='green',command= lambda: click1(3))
forth=Button(mf,text='4',fg='green',command= lambda: click1(4))
fifth=Button(mf,text='5',fg='green',command= lambda: click1(5))
sixth=Button(mf,text='6',fg='green',command= lambda: click1(6))
seventh=Button(mf,text='7',fg='green',command= lambda: click1(7))
eighth=Button(mf,text='8',fg='green',command= lambda: click1(8))
ninth=Button(mf,text='9',fg='green',command= lambda: click1(9))
zero=Button(mf,text='0',fg='green',command= lambda: click1(0))
dot=Button(mf,text='.',fg='green',command= lambda: click1("."))

# Operations
plus=Button(mf,text='+',fg='green',command= lambda: click1("+"))
minus=Button(mf,text='-',fg='green',command= lambda: click1("-"))
multip=Button(mf,text='x',fg='green',command= lambda: click1("*"))
divid=Button(mf,text='/',fg='green',command= lambda: click1("/"))
equal = Button(mf, text='=', fg='green', command=calculate)
# number placements
first.place(x=100, y=200)
second.place(x=200, y=200)
third.place(x=300, y=200)

forth.place(x=100, y=300)
fifth.place(x=200, y=300)
sixth.place(x=300, y=300)

seventh.place(x=100, y=400)
eighth.place(x=200, y=400)
ninth.place(x=300, y=400)

zero.place(x=100, y=500)
dot.place(x=200, y=500)
equal.place(x=300, y=500)
# operation placement
plus.place(x=400, y=200)
minus.place(x=400, y=300)
multip.place(x=400, y=400)
divid.place(x=400, y=500)

# scissors=Button(mf,text='Scissors',fg='green',command= lambda: click1(2))
# scissors.pack()
myroot.mainloop()