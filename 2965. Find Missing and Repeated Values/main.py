from collections import Counter


def findMissingAndRepeatedValues(grid):
    hm = [Counter(grid[i]) for i in range(len(grid))]

    for i in range(1, len(hm)):
        hm[0] += hm[i]

    second = set(range(1, len(grid) ** 2 + 1)).difference(set(hm[0].keys()))
    first = hm[0]
    for i in hm[0]:
        if hm[0][i] == 2:
            first = i
            break
    return [first, list(second)[0]]


print(findMissingAndRepeatedValues([[1, 3], [2, 2]]))
print(findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]))
