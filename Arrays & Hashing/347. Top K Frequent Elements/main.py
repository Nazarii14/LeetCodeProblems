def topKFrequent(nums, k):
    dic = {}
    for i in nums:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1

    sorted_dict = sorted(dic.items(), key=lambda x: -x[1])
    result = [sorted_dict[i][0] for i in range(k)]
    return result


print(topKFrequent([1,2,3,2,3], 2))