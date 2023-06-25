def averageValue(nums):
    arr = [i for i in nums if i % 6 == 0]
    return int(sum(arr)/len(arr)) if len(arr) > 0 else 0

print(averageValue([1,3,6,10,12,15]))
print(averageValue([1,2,4,7,10]))
