def print_matrix(matrix):
    for i in matrix:
        print(i)

def rotate_one_element(matrix, i, j):
    temp_value = matrix[i][len(matrix) - j - 1]

    matrix[i][len(matrix) - j - 1] = matrix[i][j]

    temp_value1 = matrix[len(matrix) - i - 1][len(matrix) - j - 1]
    matrix[len(matrix) - i - 1][len(matrix) - j - 1] = temp_value

    temp_value = matrix[len(matrix) - j - 1][len(matrix) - i - 1]
    matrix[len(matrix) - j - 1][len(matrix) - i - 1] = temp_value1

    matrix[i][j] = temp_value
    return matrix

def rotate(matrix):
    pass

print_matrix(rotate_one_element([[5,1,9,11],
                                 [2,4,8,10],
                                 [13,3,6,7],
                                 [15,14,12,16]], 0, 1))

# [5,13,9,11],
# [2,4,8,1],
# [12,3,6,7],
# [15,14,10,16]

