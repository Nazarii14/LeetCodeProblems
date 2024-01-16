def duplicateZeros(arr):
    result = []
    i, k = 0, 0
    while k != len(arr):
        result.append(arr[i])
        if arr[i] == 0:
            result.append(arr[i])
            k += 1
        i += 1
        k += 1
    return result


print(duplicateZeros([1,0,2,3,0,4,5,0]))
print(duplicateZeros([1,2,3]))
