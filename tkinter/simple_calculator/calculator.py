from tkinter import *

root = Tk()
root.title("Simple calculator")
root.iconbitmap('C:\\Users\\acer\\Desktop\\tkinter\\demo\\calc.ico')

entry = Entry(root, width=30, borderwidth=2, bg="#D3D3D3", justify=RIGHT)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    previous_numbers = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(previous_numbers) + str(number))


def button_clear():
    entry.delete(0, END)


def get_first_number():
    global first_number
    first_number = int(entry.get())
    entry.delete(0, END)


def button_add():
    global action
    get_first_number()
    action = "Addition"


def button_subtract():
    global action
    get_first_number()
    action = "Subtraction"


def button_multiply():
    global action
    get_first_number()
    action = "Multiplication"


def button_divide():
    global action
    get_first_number()
    action = "Division"


def button_equal():
    second_number = entry.get()
    result = first_number
    if action == "Addition":
        result += int(second_number)
    elif action == "Subtraction":
        result -= int(second_number)
    elif action == "Multiplication":
        result *= int(second_number)
    elif action == "Division":
        result /= int(second_number)

    entry.delete(0, END)
    entry.insert(0, str(result))


button_1 = Button(root, text=1, padx=30, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text=2, padx=30, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text=3, padx=30, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text=4, padx=30, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text=5, padx=30, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text=6, padx=30, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text=7, padx=30, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text=8, padx=30, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text=9, padx=30, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text=0, padx=30, pady=20, command=lambda: button_click(0))

button_clear = Button(root, text="C", padx=30, pady=20, command=button_clear)
button_add = Button(root, text="+", padx=30, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=30, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=30, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=30, pady=20, command=button_divide)
button_equal = Button(root, text="=", padx=30, pady=20, command=button_equal)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=1)

button_clear.grid(row=5, column=0)
button_add.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=5, column=3)
button_equal.grid(row=5, column=2)

root.mainloop()
