# Составить генератор (yield), который выводит из строки только цифры.

def stroka(letter):
    for i in letter:
        if i.isdigit():
            yield i

print('Цифры из строки: ', *list(stroka(input(f"Введите строку: "))))