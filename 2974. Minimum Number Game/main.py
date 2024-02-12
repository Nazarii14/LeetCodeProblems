def numberGame(nums):
    nums = sorted(nums)

    for i in range(0, len(nums) - 1, 2):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


def numberGame2(nums):
    nums.sort()
    output = []
    for i in range(0, len(nums), 2):
        output.append(nums[i + 1])
        output.append(nums[i])
    return output

import time
start = time.time()

print(numberGame2([5, 4, 2, 3]))
print(numberGame2([2, 5]))
end = time.time()
print(f"{end - start}s")  # RUNTIME 0

# 0, 1, 2, 3, 4, 5, 6, 7
# 1, 0, 3, 2, 5, 4, 7, 6
