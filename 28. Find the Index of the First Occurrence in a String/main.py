def strStr(haystack, needle):
    return haystack.index(needle) if needle in haystack else -1

print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))