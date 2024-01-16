def matrixReshape(mat, r, c):
    if r*c != len(mat) * len(mat[0]):
        return mat

    for i in range(1, len(mat)):
        mat[0] += mat[i]
        mat[i] = []
    mat = mat[0]

    result = []
    for i in range(0, r*c, c):
        l = i
        g = r
        k = mat[i:i+c]
        result.append(mat[i:i+c])
    return result


print(matrixReshape([[1, 2]], 1, 1))
print(matrixReshape([[1, 2], [3, 4], [5, 6]], 2, 3))
print(matrixReshape([[1, 2], [3, 4], [5, 6], [7, 8]], 2, 4))
