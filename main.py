import tkinter as tk

Calc = ''


def add_to_calc(symbol):
    global Calc
    Calc += str(symbol)
    text_reuslt.delete(1.0, 'end')
    text_reuslt.insert(1.0, Calc)


def evlauat_calc():
    global Calc
    print(Calc)
    try:
        Calc = str(eval(Calc))
        text_reuslt.delete(1.0, 'end')
        text_reuslt.insert(1.0, Calc)

    except:
        clear_calc()
        text_reuslt.insert(1.0, "Error")


def clear_calc():
    global Calc
    Calc = ''
    text_reuslt.delete(1.0, 'end')


window = tk.Tk()
window.geometry('300x275')
text_reuslt = tk.Text(window, height=2, width=16, font=('Arial', 24))
text_reuslt.grid(columnspan=5)

btn_1 = tk.Button(window, text='1', command=lambda: add_to_calc(1), width=5, font=('Arial', 14))
btn_1.grid(row=1, column=1)
btn_2 = tk.Button(window, text='2', command=lambda: add_to_calc(2), width=5, font=('Arial', 14))
btn_2.grid(row=1, column=2)
btn_3 = tk.Button(window, text='3', command=lambda: add_to_calc(3), width=5, font=('Arial', 14))
btn_3.grid(row=1, column=3)
btn_plus = tk.Button(window, text='+', command=lambda: add_to_calc("+"), width=5, font=('Arial', 14))
btn_plus.grid(row=1, column=4)
btn_4 = tk.Button(window, text='4', command=lambda: add_to_calc(4), width=5, font=('Arial', 14))
btn_4.grid(row=2, column=1)
btn_5 = tk.Button(window, text='5', command=lambda: add_to_calc(5), width=5, font=('Arial', 14))
btn_5.grid(row=2, column=2)
btn_6 = tk.Button(window, text='6', command=lambda: add_to_calc(6), width=5, font=('Arial', 14))
btn_6.grid(row=2, column=3)
btn_min = tk.Button(window, text='-', command=lambda: add_to_calc("-"), width=5, font=('Arial', 14))
btn_min.grid(row=2, column=4)
btn_7 = tk.Button(window, text='7', command=lambda: add_to_calc(7), width=5, font=('Arial', 14))
btn_7.grid(row=3, column=1)
btn_8 = tk.Button(window, text='8', command=lambda: add_to_calc(8), width=5, font=('Arial', 14))
btn_8.grid(row=3, column=2)
btn_9 = tk.Button(window, text='9', command=lambda: add_to_calc(9), width=5, font=('Arial', 14))
btn_9.grid(row=3, column=3)
btn_mul = tk.Button(window, text='x', command=lambda: add_to_calc("*"), width=5, font=('Arial', 14))
btn_mul.grid(row=3, column=4)
btn_open = tk.Button(window, text='(', command=lambda: add_to_calc("("), width=5, font=('Arial', 14))
btn_open.grid(row=4, column=1)
btn_0 = tk.Button(window, text='0', command=lambda: add_to_calc(0), width=5, font=('Arial', 14))
btn_0.grid(row=4, column=2)
btn_close = tk.Button(window, text=')', command=lambda: add_to_calc(")"), width=5, font=('Arial', 14))
btn_close.grid(row=4, column=3)
btn_div = tk.Button(window, text='/', command=lambda: add_to_calc("/"), width=5, font=('Arial', 14))
btn_div.grid(row=4, column=4)

btn_equal = tk.Button(window, text='=', command=evlauat_calc, width=11, font=('Arial', 14))
btn_equal.grid(row=5, column=1, columnspan=2)
btn_clear = tk.Button(window, text='C', command=clear_calc, width=11, font=('Arial', 14))
btn_clear.grid(row=5, column=3, columnspan=3)

window.mainloop()