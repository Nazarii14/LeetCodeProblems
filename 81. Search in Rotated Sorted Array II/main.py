def search(nums, target):
    if min(nums) == target:
        return True

    nums = sorted(nums)
    l, r = 0, len(nums) - 1
    while l <= r:
        middle = l + (r - l) // 2
        if nums[middle] < target:
            l = middle + 1
        elif nums[middle] > target:
            r = middle - 1
        else:
            return True
    return False




print(search([2,5,6,0,0,1,2], 0))
print(search([2,5,6,0,0,1,2], 3))
