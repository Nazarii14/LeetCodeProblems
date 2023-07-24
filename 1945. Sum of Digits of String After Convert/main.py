def getLucky(s, k):
    result = [j for i in s for j in str(ord(i) - 96)]

    for i in range(k):
        result = str(sum([int(x) for x in result]))
    return result

print(getLucky("iiii",1))
print(getLucky("leetcode",2))