def minNumber(nums1, nums2):
    length = len(nums1) if len(nums1) < len(nums2) else len(nums2)

    is_in_both_arrays = False
    in_both_arrays = -1

    for i in range(length):
        if nums1[i] in nums1 and i in nums2 and (i < in_both_arrays or not is_in_both_arrays):
            in_both_arrays = i
            is_in_both_arrays = True

    min1, min2 = min(nums1), min(nums2)
    using_arrays = min1 * 10 + min2 if min2 > min1 else min2 * 10 + min1

    if is_in_both_arrays:
        return using_arrays if using_arrays < in_both_arrays else in_both_arrays

    return using_arrays

#print(minNumber([4,1,3], [5,7]))
#print(minNumber([6,4,3,7,2,1,8,5], [6,8,5,3,1,7,4,2]))
print(minNumber([5,7,1,6,8], [2,4,6,3]))
