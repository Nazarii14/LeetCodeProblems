def merge(intervals):
    intervals = sorted(intervals, key=lambda x:x[0])

    changed = True
    while changed:
        i = 0
        res = []
        changed = False
        while i < len(intervals):
            if i != len(intervals) - 1 and intervals[i][1] >= intervals[i + 1][0]:
                res.append([min(intervals[i][0], intervals[i+1][0]), max(intervals[i + 1][1], intervals[i][1])])
                i += 2
                changed = True
            else:
                res.append(intervals[i])
                i += 1
        intervals = res
    return intervals


print(merge([[1, 3], [8, 10], [9, 18]]))
print(merge([[1, 4], [4, 5]]))
print(merge([[1, 10], [11, 12]]))
print(merge([[1, 4], [0, 0]]))
