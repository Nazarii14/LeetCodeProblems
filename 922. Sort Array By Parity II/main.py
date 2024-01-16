def sort_array_by_parity(nums):
    odd, even = [i for i in nums if i % 2 == 0], [i for i in nums if i % 2 == 1]
    result = []
    for i in range(len(odd)):
        result.append(odd[i])
        result.append(even[i])
    return result


print(sort_array_by_parity([4, 2, 5, 7]))
print(sort_array_by_parity([2, 3]))
