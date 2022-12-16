def zero_matrix(matrix):
    row_targets = []
    col_targets = []
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if col == 0:
                row_targets.append(row_index)
                col_targets.append(col_index)

    # process rows
    for row_index in range(len(matrix)):
        if row_index in row_targets:
            for col_index in range(len(matrix[row_index])):
                matrix[row_index][col_index] = 0

    # process cols
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if col_index in col_targets:
                matrix[row_index][col_index] = 0
    return matrix


print(zero_matrix([[0, 2, 3], [4, 0, 6], [7, 8, 0]]))  # all zeroes
print(zero_matrix([[1, 2, 3, 4], [5, 6], [0, 8, 9, 0, 1, 2, 3, 4, 5, 6]]))
