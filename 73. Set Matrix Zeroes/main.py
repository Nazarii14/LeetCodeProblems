def setZeroes(matrix):
    new_matrix = matrix.copy()
    for i in range(len(matrix)):
        if 0 in matrix[i]:
            new_matrix[i] = [0] * len(matrix[0])
    return new_matrix


print(setZeroes([[1,1,1],
                 [1,0,1],
                 [1,1,1]]))
print(setZeroes([[0,1,2,0],
                 [3,4,5,2],
                 [1,3,1,5]]))