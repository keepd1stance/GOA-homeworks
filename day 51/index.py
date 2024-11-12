def row_and_column_sums(matrix):
    row_sums = []  
    column_sums = [0] * len(matrix[0])  
    
    for i in range(len(matrix)):
        row_sum = 0  
        for j in range(len(matrix[i])):
            row_sum += matrix[i][j]  
            column_sums[j] += matrix[i][j]  
        row_sums.append(row_sum)  

    return row_sums, column_sums

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(row_and_column_sums(matrix))