def checkIfExist(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] == arr[i] * 2 or arr[i] == arr[j] * 2:
                return True
    return False


print(checkIfExist([-2, 0, 10, -19, 4, 6, -8]))
print(checkIfExist([10, 2, 5, 3]))
print(checkIfExist([3, 1, 7, 11]))
