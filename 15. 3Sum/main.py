def threeSum(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
    return result

def threeSum1(nums):
    n = len(nums)
    res = []
    nums.sort()
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s > 0: r -= 1
            elif s < 0: l += 1
            else:
                b = [nums[i], nums[l], nums[r]]
                if b not in res:
                    res.append(b)
                l += 1
    return res

def threeSum2(nums):
    res = set()
    n, p, z = [], [], []
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)

    N, P = set(n), set(p)

    if z:
        for num in P:
            if -1*num in N:
                res.add((-1*num, 0, num))

    if len(z) >= 3:
        res.add((0,0,0))

    for i in range(len(n)):
        for j in range(i+1,len(n)):
            target = -1*(n[i]+n[j])
            if target in P:
                res.add(tuple(sorted([n[i],n[j],target])))

    for i in range(len(p)):
        for j in range(i+1,len(p)):
            target = -1*(p[i]+p[j])
            if target in N:
                res.add(tuple(sorted([p[i],p[j],target])))

    return res


print(threeSum2([-1,0,1,2,-1,-4]))
print(threeSum2([0,1,1]))
print(threeSum2([-1,0,1,2,-1,-4]))