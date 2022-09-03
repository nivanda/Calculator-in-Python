import tkinter as tk
from tkinter import RIGHT
import math

m = ''
A = ''
B = ''
C = ''

win = tk.Tk()

top = tk.Frame()
mid = tk.Frame()
low = tk.Frame()
tools = tk.Frame()
tools2 = tk.Frame()
mem = tk.Frame()
lisad = tk.Frame()
lisad2 = tk.Frame()

button1 = tk.Button(master=top, text='1')
button2 = tk.Button(master=top, text='2')
button3 = tk.Button(master=top, text='3')
button4 = tk.Button(master=mid, text='4')
button5 = tk.Button(master=mid, text='5')
button6 = tk.Button(master=mid, text='6')
button7 = tk.Button(master=low, text='7')
button8 = tk.Button(master=low, text='8')
button9 = tk.Button(master=low, text='9')
button0 = tk.Button(text='0')
plus = tk.Button(master=tools, text='+')
minus = tk.Button(master=tools, text='-')
multi = tk.Button(master=tools, text='*')
div = tk.Button(master=tools2, text='/')
clear = tk.Button(master=tools2, text='Clear')
equals = tk.Button(master=tools2, text='=')
memA = tk.Button(master=mem, text='A')
memB = tk.Button(master=mem, text='B')
memC = tk.Button(master=mem, text='C')
binaar = tk.Button(master=lisad, text='BIN')
aste = tk.Button(master=lisad, text='xy')
ruutjuur = tk.Button(master=lisad, text='ruutjuur')
HEX = tk.Button(master=lisad2, text='HEX')

label = tk.Label(text='', height=3)

label.pack()
top.pack()
mid.pack()
low.pack()
button0.pack()
tools.pack()
tools2.pack()
mem.pack()
lisad.pack()
lisad2.pack()
button3.pack(side=RIGHT)
button2.pack(side=RIGHT)
button1.pack(side=RIGHT)
button6.pack(side=RIGHT)
button5.pack(side=RIGHT)
button4.pack(side=RIGHT)
button9.pack(side=RIGHT)
button8.pack(side=RIGHT)
button7.pack(side=RIGHT)
plus.pack(side=RIGHT)
minus.pack(side=RIGHT)
multi.pack(side=RIGHT)
div.pack(side=RIGHT)
clear.pack(side=RIGHT)
equals.pack(side=RIGHT)
memC.pack(side=RIGHT)
memB.pack(side=RIGHT)
memA.pack(side=RIGHT)
binaar.pack(side=RIGHT)
aste.pack(side=RIGHT)
ruutjuur.pack(side=RIGHT)
HEX.pack(side=RIGHT)

def main():
    button1.bind('<Button-1>', action1)
    button2.bind('<Button-1>', action2)
    button3.bind('<Button-1>', action3)
    button4.bind('<Button-1>', action4)
    button5.bind('<Button-1>', action5)
    button6.bind('<Button-1>', action6)
    button7.bind('<Button-1>', action7)
    button8.bind('<Button-1>', action8)
    button9.bind('<Button-1>', action9)
    button0.bind('<Button-1>', action0)
    plus.bind('<Button-1>', action_plus)
    minus.bind('<Button-1>', action_minus)
    multi.bind('<Button-1>', action_multi)
    div.bind('<Button-1>', action_div)
    clear.bind('<Button-1>', action_clear)
    equals.bind('<Button-1>', action_equals)
    memA.bind('<Button-1>', actionA)
    memB.bind('<Button-1>', actionB)
    memC.bind('<Button-1>', actionC)
    aste.bind('<Button-1>', action_aste)
    binaar.bind('<Button-1>', action_binaar)
    ruutjuur.bind('<Button-1>', action_ruutjuur)
    HEX.bind('<Button-1>', action_hex)
    win.mainloop()


def action1(event):
    global m
    label.config(text=m + '1')
    m += '1'
    main()
def action2(event):
    global m
    label.config(text=m + '2')
    m += '2'
    main()
def action3(event):
    global m
    label.config(text=m + '3')
    m += '3'
    main()
def action4(event):
    global m
    label.config(text=m + '4')
    m += '4'
    main()
def action5(event):
    global m
    label.config(text=m + '5')
    m += '5'
    main()
def action6(event):
    global m
    label.config(text=m + '6')
    m += '6'
    main()
def action7(event):
    global m
    label.config(text=m + '7')
    m += '7'
    main()
def action8(event):
    global m
    label.config(text=m + '8')
    m += '8'
    main()
def action9(event):
    global m
    label.config(text=m + '9')
    m += '9'
    main()
def action0(event):
    global m
    label.config(text=m + '0')
    m += '0'
    main()
def action_plus(event):
    global m
    label.config(text=m + ' + ')
    m += ' + '
    main()
def action_minus(event):
    global m
    label.config(text=m + ' - ')
    m += ' - '
    main()
def action_multi(event):
    global m
    label.config(text=m + ' * ')
    m += ' * '
    main()
def action_div(event):
    global m
    label.config(text=m + ' / ')
    m += ' / '
    main()
def action_clear(event):
    global m
    label.config(text='')
    m = ''
    main()
def action_equals(event):
    label.config(text=eval(m))
    main()

def actionA(event):
    global m, A
    if A != '':
        label.config(text=m + str(A))
        m += str(A)
        main()
    else:
        A = eval(m)
        main()
def actionB(event):
    global m, B
    if B != '':
        label.config(text=m + str(B))
        m += str(B)
        main()
    else:
        B = eval(m)
        main()
def actionC(event):
    global m, C
    if C != '':
        label.config(text=m + str(C))
        m += str(C)
        main()
    else:
        C = eval(m)
        main()
def action_aste(event):
    global m
    label.config(text=m + ' ** ')
    m += ' ** '
    main()
def action_binaar(event):
    global m
    n = bin(int(m))
    nlist = list(n)
    nlist.remove('0')
    nlist.remove('b')
    sep = ''
    label.config(text=sep.join(nlist))
    main()
def action_ruutjuur(event):
    global m
    label.config(text=math.sqrt(int(m)))
    main()
def action_hex(event):
    global m
    n = hex(int(m))
    nlist = list(n)
    nlist.remove('0')
    nlist.remove('x')
    sep = ''
    label.config(text=sep.join(nlist))
    main()


main()