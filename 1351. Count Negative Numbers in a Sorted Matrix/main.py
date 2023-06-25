def countNegatives(grid):
    result = 0
    for i in grid:
        result += len([j for j in i if j < 0])
    return result

print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))