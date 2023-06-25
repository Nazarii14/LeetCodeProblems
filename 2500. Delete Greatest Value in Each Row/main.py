def deleteGreatestValue(grid):
    for i in range(len(grid)):
        grid[i] = sorted(grid[i], reverse=True)

    result = 0

    for j in range(len(grid[0])):
        result += max([grid[i][0] for i in range(len(grid))])
        grid = [i[1:] for i in grid]
    return result



print(deleteGreatestValue([[1, 2, 4], [3, 3, 1]]))
print(deleteGreatestValue([[10]]))
