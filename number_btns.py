from tkinter import *


number_click = Entry(width=40, font=('Lato', 10))
number_click.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def click_number(number):
    number_click.insert(END, number)
