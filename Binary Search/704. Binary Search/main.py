def search(nums, target):
    if len(nums) == 1 and nums[0] == target:
        return 0
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + (r - l)//2
        if target < nums[(l+r)//2]:
            r = m - 1
        elif target > nums[(l+r)//2]:
            l = m + 1
        else:
            return m
    return -1

print(search([2,5], 5))

