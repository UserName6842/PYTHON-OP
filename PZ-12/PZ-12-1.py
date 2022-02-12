from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Форма Заявки")
window.geometry("550x500")

zagolovok = Label(text = "Форма заявки", bg = '#308f49', fg = "white", padx = '500', pady = '1', font = ('Arial', 10 ))
zagolovok.place(x=-250, y=20)

d = Label(text="Допустимые типы вложений: .zip, .rar, .txt, .doc, .jpg, .png, .gif, .odt, .xml", fg='black', bg='#D3D3D3', padx='200', pady='5',  font=('Arial', 10))
d.place(x=-190, y=42)
m = Label(text="Макс. размер каждого файла: 1024kb", fg='black', bg='#D3D3D3', padx='500', pady='5', font=('Arial', 10))
m.place(x=-490, y=72)
a = Label(text="Макс. общий размер файла: 2048kb", fg='black', bg='#D3D3D3', padx='500', pady='5', font=('Arial', 10))
a.place(x=-490, y=102)


name = Label(text = "Ваше имя:", bg='#D3D3D3', fg='black', padx='500', pady='5', font=('Arial', 10))
name.place(x=-490, y=133)

email = Label(text = "Ваш Email:", bg='#D3D3D3', fg='black', padx='500', pady='5', font=('Arial', 10))
email.place(x=-490, y=163)

massage = Label(text = "Тема письма:", bg='#D3D3D3', fg='black', padx='500', pady='5', font=('Arial', 10))
massage.place(x=-490, y=193)

file1 = Label(text = "Прикрепить файл:", bg='#D3D3D3', fg='black', padx='500', pady='5', font=('Arial', 10))
file1.place(x=-490, y=223)

file2 = Label(text = "Прикрепить файл:", bg='#D3D3D3', fg='black', padx='500', pady='5', font=('Arial', 10))
file2.place(x=-490, y=253)

file3 = Label(text = "Прикрепить файл:", bg='#D3D3D3', fg='black', padx='500', pady='5', font=('Arial', 10))
file3.place(x=-490, y=283)

your_massahe = Label(text = "Ваше сообщение:", bg='#D3D3D3', fg='black', padx='500', pady='5', font=('Arial', 10))
your_massahe.place(x=-490, y=313)


Entry(textvariable=StringVar(value=''), fg='black', width=32, font='arial 10').place(x=150, y=137)    # Имя.

Entry(textvariable=StringVar(value=''), fg='black', width=32, font='arial 10').place(x=150, y=167)    # Email.

Entry(textvariable=StringVar(value=''), fg='black', width=32, font='arial 10').place(x=150, y=197)    # Тема письма.

Entry(textvariable=StringVar(value=''), fg='black', width=32, font='arial 10').place(x=150, y=227)    # Файл1.
Button(text="Обзор...", bg='#D3D3D3', fg='black', width=10, font='Arial 7').place(x=380, y=228)

Entry(textvariable=StringVar(value=''), fg='black', width=32, font='arial 10').place(x=150, y=257)    # Файл2.
Button(text="Обзор...", bg='#D3D3D3', fg='black', width=10, font='Arial 7').place(x=380, y=258)

Entry(textvariable=StringVar(value=''), fg='black', width=32, font='arial 10').place(x=150, y=287)    # Файл3.
Button(text="Обзор...", bg='#D3D3D3', fg='black', width=10, font='Arial 7').place(x=380, y=288)

text = Text(window, height=8, width=60)    # Скроллбар.
text.pack(side='left')
scrollbar = Scrollbar(window)
scrollbar.place(x=523, y=390)
scrollbar['command'] = text.yview
text['yscrollcommand'] = scrollbar.set
text.place(x=40, y=343)

zagolovok1 = Label(bg = '#308f49', padx = '500', pady = '3',)
zagolovok1.place(x=-250, y=475)

Button(text="Отправить Email", bg='#D3D3D3', fg='black', width=15, font='Arial 9').place(x=135, y=475)
Button(text="Отчислить", bg='#D3D3D3', fg='black', width=15, font='Arial 9').place(x=250, y=475)


window.mainloop()