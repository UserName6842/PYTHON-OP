# В исходном текстовом файле (Dostoevsky.txt) найти все произведения писателя.
# Посчитать количество полученных элементов.
# « »

import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    Dostoevsky = file.read()
    new_list = re.findall(r"«\w+»", Dostoevsky)
    a = set(new_list)
    print(set(new_list))
    print(f'Количество произведений Достоевского: {len(a)}')
