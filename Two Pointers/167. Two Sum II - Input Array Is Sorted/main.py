def twoSum(numbers, target):
    l, r = 0, len(numbers)-1

    while l < r:
        curSum = numbers[l] + numbers[r]
        if curSum < target:
            l += 1
        elif curSum > target:
            r -= 1
        else:
            return [l+1, r+1]


print(twoSum([1, 2, 3, 4, 5, 6], 7))