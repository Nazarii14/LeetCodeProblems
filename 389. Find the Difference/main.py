def findTheDifference(s, t):
    sum_s = sum([ord(i) for i in s])
    sum_t = sum([ord(i) for i in t])
    return chr(sum_t - sum_s)

print(findTheDifference("abcd", "abcde"))