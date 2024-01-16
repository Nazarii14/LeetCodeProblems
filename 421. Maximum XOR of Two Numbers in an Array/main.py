def findMaximumXOR(nums):
    max_xor = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            curr_xor = i ^ j
            max_xor = max(curr_xor, max_xor)
    return max_xor

print(findMaximumXOR([3,10,5,25,2,8]))
print(findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))
