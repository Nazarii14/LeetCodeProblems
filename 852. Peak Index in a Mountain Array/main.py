def peakIndexInMountainArray(arr):
    l, r = 0, len(arr) - 1

    while l < r:
        middleIndex = l + (r - l) // 2
        if arr[middleIndex - 1] < arr[middleIndex] and arr[middleIndex] > arr[middleIndex + 1]:
            return middleIndex
        elif arr[middleIndex - 1] > arr[middleIndex]:
            r = middleIndex
        elif arr[middleIndex] < arr[middleIndex + 1]:
            l = middleIndex

    return min(l, r)

print(peakIndexInMountainArray([0,1,0]))
print(peakIndexInMountainArray([0,2,1,0]))
print(peakIndexInMountainArray([0,10,5,2]))
print(peakIndexInMountainArray([0,10,15,20,1]))
print(peakIndexInMountainArray([3,9,8,6,4]))
