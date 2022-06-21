# В матрице найти сумму элементов второй половины матрицы.

import random
row = 4
columns = 4

matrix = [[random.randint(1, 11) for y in range(columns)] for x in range(row)]
for i in matrix:
    print(i)

sum = 0

n = range(int(row / 2))
n = list(n)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j in n:
            sum += matrix[i][j]

print()
print(sum)
