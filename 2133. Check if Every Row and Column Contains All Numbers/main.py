def checkValid(matrix):
    length = len(matrix)
    trans = [[matrix[i][j] for i in range(length)] for j in range(length)]
    for i in matrix:
        if sorted(i) != list(range(1, length + 1)):
            return False
    for i in trans:
        if sorted(i) != list(range(1, length + 1)):
            return False
    return True


print(checkValid([[1,2,3],[3,1,2],[2,3,1]]))
print(checkValid([[1,1,1],[1,2,3],[1,2,3]]))
print(checkValid([[1,1,1],[1,2,3],[1,2,3]]))
