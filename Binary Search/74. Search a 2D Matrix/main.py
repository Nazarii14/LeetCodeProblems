# def searchMatrix(matrix, target):
#     if len(matrix) == 1:
#         return target in matrix[0]
#
#     for i in range(len(matrix)):
#         if matrix[i][0] == target:
#             return True
#         elif matrix[i][0] > target:
#             return False if i == 0 else target in matrix[i-1]
#
#         if i == len(matrix) - 1:
#             return target in matrix[len(matrix) - 1]
#     return False

def searchMatrix(matrix, target):
    for i in matrix:
        if target in i:
            return True
    return False


print(searchMatrix([[1]], 1))

