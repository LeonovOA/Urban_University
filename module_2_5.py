def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)

    return matrix

result = get_matrix(4, 2, 12)
print(result)
