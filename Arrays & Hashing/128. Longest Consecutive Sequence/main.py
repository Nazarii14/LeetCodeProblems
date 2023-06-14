def longestConsecutive(nums):
    nums = sorted(list(set(nums)))
    result_arr, temp_arr = [], []

    for i in nums:
        if len(temp_arr) == 0:
            temp_arr.append(i)
        elif temp_arr[-1] + 1 == i:
            temp_arr.append(i)
        else:
            if len(result_arr) < len(temp_arr):
                result_arr = temp_arr
            temp_arr = [i]

    if len(result_arr) < len(temp_arr):
        result_arr = temp_arr
    return len(result_arr)

print(longestConsecutive([1,2,0,1]))