def heightChecker(heights):
    srt = sorted(heights)
    result = 0
    for i in range(len(heights)):
        result += heights[i] != srt[i]
    return result

print(heightChecker([1,1,4,2,1,3]))