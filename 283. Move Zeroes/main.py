def moveZeroes(nums):
    length = len(nums)

    while 0 in nums:
        nums.remove(0)

    nums += [0] * (length - len(nums))
    return nums

print(moveZeroes([0,1,0,3,12]))