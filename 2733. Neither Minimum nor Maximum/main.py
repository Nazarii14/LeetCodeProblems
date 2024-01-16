def findNonMinOrMax(nums):
    min_ = min(nums)
    max_ = max(nums)

    for i in nums:
        if i == min_ or i == max_:
            continue
        else:
            return i
    return -1

print(findNonMinOrMax([3, 2, 1, 4]))
print(findNonMinOrMax([2, 1]))
print(findNonMinOrMax([3, 2, 1]))
