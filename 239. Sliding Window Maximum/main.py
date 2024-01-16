import collections
def maxSlidingWindow(nums, k):
    res = []
    q = collections.deque()
    l = r = 0
    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()

        if (r + l) >= k:
            res.append(nums[q[0]])
            l += 1
        r += 1

    return res





print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(maxSlidingWindow([1], 1))
