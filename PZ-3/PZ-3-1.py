# Даны числа х, у. Проверить истинность высказывания:
# «Точка с координатами (х, у) лежит во второй координатной четверти».

# Вводим значения переменной X.
x = input("Введите значение X: ")

# Исключение.
while type(x) != float:
    try:
        x = float(x)
    except ValueError:
        print("к сожалению буквы не являются цифрами(")
        x = input("Введите значение X: ")

y = input("Введите значение Y: ")

# Исключение.
while type(y) != float:
    try:
        y = float(y)
    except ValueError:
        print("к сожалению буквы не являются цифрами(")
        y = input("Введите значение Y: ")

# Условия
if (x > 0) and (y > 0):
    print("Точка лежит в I половине координатной плоскости")

elif (x < 0) and (y > 0):
    print("Точка лежит во II половине координатной плоскости\nTRUE")

elif (x < 0) and (y < 0):
    print("Точка лежит в III половине координатной плоскости")

elif (x > 0) and (y < 0):
    print("Точка лежит в IV половине координатной плоскости")