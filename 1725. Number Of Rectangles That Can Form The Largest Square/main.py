def countGoodRectangles(rectangles):
    minimums = [min(i) for i in rectangles]
    return minimums.count(max(minimums))

print(countGoodRectangles([[5,8],[3,9],[5,12],[16,5]]))

