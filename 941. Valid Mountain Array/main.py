def validMountainArray(arr):
    if len(arr) < 3:
        return False

    if arr.count(max(arr)) > 1:
        return False

    idx = arr.index(max(arr))
    if sorted(list(set(arr[:idx]))) == [] or sorted(list(set(arr[idx + 1:]))) == []:
        return False

    if arr[:idx] != sorted(list(set(arr[:idx]))) or arr[idx + 1:] != sorted(list(set(arr[idx + 1:])), reverse=True):
        return False
    return True


print(validMountainArray([2, 1]))
print(validMountainArray([2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(validMountainArray([1, 5, 5]))
print(validMountainArray([0, 3, 2, 1]))
