def duplicateZeros(arr):
    # result = []
    # for i in arr:
    #     result.append(i)
    #     if i == 0:
    #         result.append(i)
    #     if len(result) == len(arr):
    #         return result
    #
    # return result
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == 0:
            arr = arr[:i + 1] + [0] + arr[i + 1:-1]
            i += 1
        i += 1
    return arr


print(duplicateZeros([1,0,2,3,0,4,5,0]))
print(duplicateZeros([1,2,3]))
