def matrix_sum(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

matrix1 = [[1, 3], [1, 4]]
matrix2 = [[4, 1], [2, 2]]
print(matrix_sum(matrix1, matrix2))



def transpose(matrix):
    transposed_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        transposed_matrix.append(new_row)
    return transposed_matrix

matrix = [[1, 2, 3], [4, 5, 6]]
print(transpose(matrix))



def diagonal_sums(matrix):
    n = len(matrix)
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0 

    for i in range(n):
        main_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][n - i - 1]

    return main_diagonal_sum, secondary_diagonal_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonal_sums(matrix))