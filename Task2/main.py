def max_sum_square(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    max_sum = float('-inf')  # Очень большое отрицательное число
    max_square = None  # Пустой квадрат

    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    size = min(k - i + 1, l - j + 1)  # Определяем размер текущего квадрата
                    current_sum = 0
                    for x in range(i, i + size):
                        for y in range(j, j + size):
                            current_sum += matrix[x][y]

                    if current_sum > max_sum:
                        max_sum = current_sum
                        max_square = [[matrix[x][y] for y in range(j, j + size)] for x in range(i, i + size)]

    return max_square


matrix = [
    [1, -2, 3],
    [4, 5, -6],
    [-7, 8, 9]
]

result = max_sum_square(matrix)
for row in result:
    print(row)
