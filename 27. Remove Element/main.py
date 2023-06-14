def removeElement(nums, val):
    return sum([True if i != val else False for i in nums])

print(removeElement([3,2,2,3], 3))