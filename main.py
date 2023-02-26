from tkinter import *
import math

window = Tk()

window.title("Z's Calc")
window.config(background="white")
size = 45
sol = ""
ERROR = False
lastExpr = ""
w = 3
def equals():
    global sol
    global lastExpr
    if entry.get() == "ERROR":
        entry.delete(0, END)
        return 0

    if sol == entry.get():
        sol += lastExpr
    else:
        sol = entry.get()

    try:
        count = 0
        for j in range(1,len(sol)):
            if sol[j] in ["^","÷", "x", "+", "-", " mod "]:
                count += 1
                lastExpr = sol[j:]
                if count > 1:
                    lastExpr = ""
                    break

        sol = sol.replace("÷", "/")
        sol = sol.replace("x", "*")
        sol = sol.replace("^", "**")
        sol = sol.replace(" mod ", "%")
        sol = str(eval(sol))

    except (ZeroDivisionError, SyntaxError) as e:
        global ERROR
        ERROR = True
        sol = "ERROR"

    entry.delete(0, END)
    entry.insert(0, sol)


entry = Entry(window, font = ("Ariel", size))
entry.grid(column = 0, row =0, columnspan= 6)

def enter(x):
    global ERROR
    if ERROR:
        ERROR = False
        entry.delete(0, END)

    entry.insert(END, str(x))

def inverse():
    try:
        global lastExpr
        inv = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, "1÷(" + str(inv) + ")")
        equals()
        lastExpr = ""
    except SyntaxError:
        pass

def sign():
    try:
        if entry.get()[0] == "-":
            entry.delete(0, 1)
        else:
            entry.insert(0, "-(")
            entry.insert(END, ")")
    except IndexError:
        pass

def ceil():
    try:
        global lastExpr
        c = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(math.ceil(c)))
        equals()
        lastExpr = ""
    except SyntaxError:
        pass

def floor():
    global lastExpr
    try:
        f = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(math.floor(f)))
        equals()
        lastExpr = ""
    except SyntaxError:
        pass

def factorial():
    global lastExpr
    try:
        f = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(math.factorial(f)))
        equals()
        lastExpr = ""
    except SyntaxError:
        pass


for i in range(1,11):
    s = i-1
    if i == 10:
        i,s = 0,  10
    B = Button(window, text=str(i), font=("Ariel", size), width = w, height = 1, command= lambda x=i : enter(x), bg = "#ACA7AE")
    B.grid(column = s%3, row = s//3 + 1)

DotButton = Button(window, text= "." , font=("Ariel", size), width = w, height = 1, command= lambda :  entry.insert(END, str(".")), bg = "#ACA7AE")
DotButton.grid(column = 0, row = 4)

AddButton = Button(window, text= "+" , font=("Ariel", size), width = w, height = 1, command= lambda :  entry.insert(END, str("+")), bg = "#33FFD7")
AddButton.grid(column = 3, row = 1)

SubButton = Button(window, text= "-" , font=("Ariel", size), width = w, height = 1, command=  lambda :  entry.insert(END, str("-")), bg = "#33FFD7")
SubButton.grid(column = 3, row = 2)

MulButton = Button(window, text= "x" , font=("Ariel", size), width = w, height = 1, command=  lambda :  entry.insert(END, str("x")), bg = "#33FFD7")
MulButton.grid(column = 4, row = 1)

DivButton = Button(window, text= "÷" , font=("Ariel", size), width = w, height = 1, command=  lambda :  entry.insert(END, str("÷")), bg = "#33FFD7")
DivButton.grid(column = 4, row = 2)

PowerButton = Button(window, text= "^" , font=("Ariel", size), width = w, height = 1, command=  lambda :  entry.insert(END, str("^")), bg = "#33FFD7")
PowerButton.grid(column = 3, row = 3)

PowerButton = Button(window, text= "mod" , font=("Ariel", size), width = w, height = 1, command=  lambda :  entry.insert(END, str(" mod ")), bg = "#33FFD7")
PowerButton.grid(column = 4, row = 3)

FactorialButton = Button(window, text= "x!" , font=("Ariel", size), width = w, height = 1, command=  factorial, bg = "#33FFD7")
FactorialButton.grid(column = 6, row = 2)

PowerButton = Button(window, text= "⌈x⌉" , font=("Ariel", size), width = w, height = 1, command=  ceil, bg = "#33FFD7")
PowerButton.grid(column = 5, row = 3)


PowerButton = Button(window, text= "⌊x⌋" , font=("Ariel", size), width = w, height = 1, command=  floor, bg = "#33FFD7")
PowerButton.grid(column = 6, row = 3)

ClearButton = Button(window, text= "C" , font=("Ariel", size), width = w, height = 1, command=  lambda :  entry.delete(0,END), bg = "#CC5D10")
ClearButton.grid(column = 3, row = 4)

DelButton = Button(window, text= "del" , font=("Ariel", size), width = w, height = 1, command=  lambda :  entry.delete(len(entry.get())-1,END), bg = "#CC5D10")
DelButton.grid(column = 2, row = 4)

OpenButton = Button(window, text= "(" , font=("Ariel", size), width = w, height = 1, command=  lambda :  entry.insert(END, "("), bg = "#33FFD7")
OpenButton.grid(column = 5, row = 1)

CloseButton = Button(window, text= ")" , font=("Ariel", size), width = w, height = 1, command=  lambda :  entry.insert(END, ")"), bg = "#33FFD7")
CloseButton.grid(column = 6, row = 1)

InverseButton = Button(window, text= "1/x" , font=("Ariel", size), width = w, height = 1, command=  inverse, bg = "#33FFD7")
InverseButton.grid(column = 5, row = 2)

SignButton = Button(window, text= "±" , font=("Ariel", size), width = w, height = 1, command = sign, bg = "#33FFD7")

SignButton.grid(column = 4, row = 4)


EquButton = Button(window, text= "=" , font=("Ariel", size+1), width = w*2, height = 1, command= equals, bg = "#5FB5F0")
EquButton.grid(column = 5, row =4, columnspan = 2)

window.mainloop()


