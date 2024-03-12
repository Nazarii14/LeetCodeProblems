def find_binary(nums, value):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + (r - l) // 2
        if nums[m] > value:
            r = m - 1
        elif nums[m] < value:
            l = m + 1
        else:
            return True
    return False


def findIntersectionValues(nums1, nums2):
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)

    res1, res2 = 0, 0

    for i in nums1:
        res1 += find_binary(nums2, i)

    for i in nums2:
        res2 += find_binary(nums1, i)

    return [res1, res2]


def findIntersectionValues1(nums1, nums2):
    res1, res2 = 0, 0
    for i in nums1:
        res1 += i in nums2
    for i in nums2:
        res2 += i in nums1
    return [res1, res2]

print(findIntersectionValues(nums1=[4, 3, 2, 3, 1], nums2=[2, 2, 5, 2, 3, 6]))
print(findIntersectionValues(nums1=[3, 4, 2, 3], nums2=[1, 5]))
