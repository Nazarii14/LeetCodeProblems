def canMakeArithmeticProgression(arr):
    arr = sorted(arr)
    step = arr[1] - arr[0]

    for i in range(1, len(arr) - 1):
        if arr[i+1] - arr[i] != step:
            return False
    return True


print(canMakeArithmeticProgression([3,5,1]))
print(canMakeArithmeticProgression([1,2,4]))
