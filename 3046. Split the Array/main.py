def isPossibleToSplit(nums):
    nums = sorted(nums)
    count_curr = 1
    curr = nums[0]
    true = False
    false = True
    for i in range(1, len(nums)):
        if nums[i] == curr:
            count_curr += 1
        else:
            curr = nums[i]
            count_curr = 1
        if count_curr >= 3:
            return true

    return false


# print(isPossibleToSplit([1,1,2,2,3,4]))
# print(isPossibleToSplit([1,1,1,1]))
print(isPossibleToSplit([5,9,5,5,6,8,6,1,5,7]))