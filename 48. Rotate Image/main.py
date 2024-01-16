def print_matrix(matrix):
    for i in matrix:
        print(i)

def rotate_one_element(matrix, i, j):
    temp_value = matrix[j][len(matrix) - i - 1]
    matrix[j][len(matrix) - i - 1] = matrix[i][j]
    temp_value1 = matrix[len(matrix) - i - 1][len(matrix) - j - 1]
    matrix[len(matrix) - i - 1][len(matrix) - j - 1] = temp_value
    temp_value = matrix[len(matrix) - j - 1][i]
    matrix[len(matrix) - j - 1][i] = temp_value1
    matrix[i][j] = temp_value
    return matrix

def rotate(matrix):
    j_range = len(matrix) // 2
    if len(matrix) % 2 == 1:
        j_range += 1
    for i in range(len(matrix[0]) // 2):
        for j in range(j_range):
            rotate_one_element(matrix, i, j)
    return matrix


print_matrix(rotate([[5,1,9,11],
                     [2,4,8,10],
                     [13,3,6,7],
                     [15,14,12,16]]))

print_matrix(rotate([[1,2,3],[4,5,6],[7,8,9]]))

# [5,13,9,11],
# [2,4,8,1],
# [12,3,6,7],
# [15,14,10,16]

