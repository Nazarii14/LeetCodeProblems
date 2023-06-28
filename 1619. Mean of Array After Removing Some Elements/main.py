def trimMean1(arr):
    arr = sorted(arr)
    five_percent = len(arr) // 20
    arr = arr[five_percent : len(arr) - five_percent]
    return sum(arr) / len(arr)

def trimMean2(arr):
    n = int(0.05 * len(arr))
    for i in range(n):
        arr.remove(min(arr))
        arr.remove(max(arr))
    return sum(arr) / len(arr)

print(trimMean1([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]))
print(trimMean2([6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]))
print(trimMean1([6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]))
