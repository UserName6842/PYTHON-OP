from tkinter import *


def seconds(event):

    a = str

    n = int(num1.get())

    if n < 3600:
       a = "Не прошло и часа"

    elif n > 86400:
       a = "В сутках всего лишь 24 часа"

    else:
        a = n // 3600
        a = "Количество полных пройденых часов: ", a

    negative['text'] = a


root = Tk()
root.title("Секундомер")
root.geometry("420x300")

Label(text="Ввдите кол-во\nпройденых секунд").grid(row=1, column=0)
num1 = Entry()
num1.grid(row=1, column=1)

button1 = Button(text="Посчтитать")
button1.grid(row=4, column=1)

negative = Label()
negative.grid(row=6, column=1)

button1.bind('<Button-1>', seconds)

root.mainloop()