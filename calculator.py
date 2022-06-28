from tkinter import *


root = Tk()
root.title('Calculator App')
root.config(padx=30, pady=30)


# functions
def click_number(number):
    number_click.insert(END, number)


def clear():
    number_click.delete(0, END)


def equal():
    results = str(eval(number_click.get()))
    number_click.delete(0, END)
    number_click.insert(0, results)


def remove_number():
    pass


# Entry
number_click = Entry(width=40, font=('Lato', 10))
number_click.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# operand buttons
button_add = Button(root, text='+', padx=20, pady=20,
                    bg='#06C1CF', command=lambda: click_number('+'))
button_add.grid(row=4, column=3, pady=10, padx=10)

button_subtract = Button(root, text='-', padx=20, pady=20,
                         bg='#06C1CF', command=lambda: click_number('-'))
button_subtract.grid(row=3, column=3, pady=10, padx=10)

button_multiply = Button(root, text='×', padx=20, pady=20,
                         bg='#06C1CF', command=lambda: click_number('*'))
button_multiply.grid(row=2, column=3, pady=10, padx=10)

button_divide = Button(root, text='÷', padx=20, pady=20,
                       bg='#06C1CF', command=lambda: click_number('/'))
button_divide.grid(row=1, column=3, pady=10, padx=10)

button_ac = Button(root, text='AC', padx=60, pady=20,
                   bg='#F29E2C', command=clear)
button_ac.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

button_delete = Button(root, text='←', padx=20, pady=20,
                       bg='#06C1CF', command=remove_number)
button_delete.grid(row=1, column=2, pady=10, padx=10)

button_equals = Button(root, text='=', padx=60, pady=20,
                       bg='#F29E2C', command=equal)
button_equals.grid(row=5, column=2, columnspan=2, pady=10, padx=10)

# Number buttons
button_1 = Button(root, text='1', padx=20, pady=20, bg='black',
                  fg='white', command=lambda: click_number(1))
button_1.grid(row=4, column=0, pady=10, padx=10)
button_2 = Button(root, text='2', padx=20, pady=20, bg='black',
                  fg='white', command=lambda: click_number(2))
button_2.grid(row=4, column=1, pady=10, padx=10)
button_3 = Button(root, text='3', padx=20, pady=20, bg='black',
                  fg='white', command=lambda: click_number(3))
button_3.grid(row=4, column=2, pady=10, padx=10)

button_4 = Button(root, text='4', padx=20, pady=20, bg='black',
                  fg='white', command=lambda: click_number(4))
button_4.grid(row=3, column=0, pady=10, padx=10)
button_5 = Button(root, text='5', padx=20, pady=20, bg='black',
                  fg='white', command=lambda: click_number(5))
button_5.grid(row=3, column=1, pady=10, padx=10)
button_6 = Button(root, text='6', padx=20, pady=20, bg='black',
                  fg='white', command=lambda: click_number(6))
button_6.grid(row=3, column=2, pady=10, padx=10)

button_7 = Button(root, text='7', padx=20, pady=20, bg='black',
                  fg='white', command=lambda: click_number(7))
button_7.grid(row=2, column=0, pady=10, padx=10)
button_8 = Button(root, text='8', padx=20, pady=20, bg='black',
                  fg='white', command=lambda: click_number(8))
button_8.grid(row=2, column=1, pady=10, padx=10)
button_9 = Button(root, text='9', padx=20, pady=20, bg='black',
                  fg='white', command=lambda: click_number(9))
button_9.grid(row=2, column=2, pady=10, padx=10)

button_dot = Button(root, text='.', padx=20, pady=20, bg='black', fg='white')
button_dot.grid(row=5, column=1, pady=10, padx=10)
button_0 = Button(root, text='0', padx=20, pady=20, bg='black',
                  fg='white', command=lambda: click_number(0))
button_0.grid(row=5, column=0, pady=10, padx=10)


root.mainloop()
