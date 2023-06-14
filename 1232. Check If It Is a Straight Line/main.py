def checkStraightLine(coordinates):
    x1 = coordinates[0][0]
    x2 = coordinates[1][0]
    y1 = coordinates[0][1]
    y2 = coordinates[1][1]

    for i in coordinates:
        if (i[0] - x1) * (y2 - y1) != (i[1] - y1) * (x2 - x1):
            return False
    return True


print(checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
print(checkStraightLine([[0,0],[0,1],[0,-1]]))