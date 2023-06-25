def diagonalSum(mat):
    result = 0
    for i in range(len(mat)):
        result += mat[i][i]
        result += mat[i][len(mat) - i - 1]

    return result - mat[len(mat) // 2][len(mat) // 2] if len(mat) % 2 == 1 else result


print(diagonalSum([[1,2,3, 4],[4,5,6,4],[7,8,9, 4]]))
print(diagonalSum([[7,3,1,9],
                   [3,4,6,9],
                   [6,9,6,6],
                   [9,5,8,5]]))
print(diagonalSum([[1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1]]))