# Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,
# Италия . РейнаТур – Англия,Япония,Канада,ЮАР. Определить:
# 1. какие туры из Вояж, отсутствуют в РейнаТур.
# 2. какие туры из РейнаТур, отсутствуют в Вояж
# 3. перечень одинаковых туров.
# 4. равны ли перечни туров.

# Перечень туров в туристических агенствах.
Voyage = {'Мексика', 'Канада', 'Израиль', 'Италия'}
ReinaTyr = {'Англия', 'Япония', 'Канада', 'ЮАР'}

print("Вояж – Мексика, Канада, Израиль, Италия")
print("РейнаТур – Англия, Япония, Канада, ЮАР")
print()    # Пустой принт для переноса строки.

# Для Вояж.
if 'Мексика' in ReinaTyr:
    print("В РейнаТур есть путевка в Мексику")
elif 'Канада' in ReinaTyr:
    print("В РейнаТур есть путевка в Канада")
elif 'Израиль' in ReinaTyr:
    print("В РейнаТур есть путевка в Израиль")
elif 'Италия' in ReinaTyr:
    print("В РейнаТур есть путевка в Италия")

# Для РейнаТур.
if 'Англия' in Voyage:
    print("В Voyage есть путевка в Англия")
elif 'Япония' in Voyage:
    print("В Voyage есть путевка в Япония")
elif 'Канада' in Voyage:
    print("В Voyage есть путевка в Канада")
elif 'ЮАР' in Voyage:
    print("В Voyage есть путевка в ЮАР")

print()    # Пустой принт для переноса строки.
print("Перечень одинаковых туров ", Voyage & ReinaTyr)
print()    # Пустой принт для переноса строки.
print("Перечни туров не равны", Voyage != ReinaTyr)

# Всю программу можно было выполнить использовав 4 принта, вместо двух блоков с условиями.