# В матрице элементы второго столбца возвести в квадрат.

import random
row = 4
columns = 4

matrix = [[random.randint(1, 11) for y in range(columns)] for x in range(row)]
for i in matrix:
    print(i)

sum = 0



for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j == 1:
            matrix[i][j] = matrix[i][j] ** 2

print()

for i in matrix:
    print(i)