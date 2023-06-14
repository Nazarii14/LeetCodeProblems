def removeElement(nums, val):
    max_num = max(nums)
    nums = [i if i != val else max_num+1 for i in nums]
    nums = sorted(nums)
    nums = [i if i != max_num+1 else "_" for i in nums]

    return len(nums) - nums.count("_"), nums

print(removeElement([3, 2, 2, 3], 3))