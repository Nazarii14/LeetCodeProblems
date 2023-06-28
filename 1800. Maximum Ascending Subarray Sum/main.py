def maxAscendingSum(nums):
    result_subarray = []
    temp_subarray = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i-1] >= nums[i]:
            if sum(temp_subarray) > sum(result_subarray):
                result_subarray = temp_subarray
            temp_subarray = []
        temp_subarray.append(nums[i])

    if sum(temp_subarray) > sum(result_subarray):
        result_subarray = temp_subarray
    return sum(result_subarray)


#print(maxAscendingSum([10,20,30,5,10,50]))
#print(maxAscendingSum([10,20,30,40,50]))
#print(maxAscendingSum([12,17,15,13,10,11,12]))
#print(maxAscendingSum([3,6,10,1,8,9,9,8,9]))
print(maxAscendingSum([1, 1]))
