def rotate_matrix(matrix):

    # swap along the 45 degree axis
    for row_index in range(len(matrix)-1):
        for col_index in range(len(matrix[row_index])-1):

            orig = matrix[row_index][col_index]
            swap = matrix[len(matrix)-1-col_index][len(matrix)-1-row_index]
            matrix[row_index][col_index] = swap
            matrix[len(matrix)-1-col_index][len(matrix)-1-row_index] = orig

    # swap along horizontal axis to complete the rotation
    for row_index in range(len(matrix)//2):
        for col_index in range(len(matrix[row_index])):
            orig = matrix[row_index][col_index]
            swap = matrix[len(matrix)-1-row_index][col_index]
            matrix[row_index][col_index] = swap
            matrix[len(matrix)-1-row_index][col_index] = orig

    return matrix


print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate_matrix([[1, 2], [3, 4, ]]))
