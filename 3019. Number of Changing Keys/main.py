def countKeyChanges(s):
    s = s.lower()
    res = 0
    for i in range(1, len(s)):
        res += s[i] != s[i-1]
    return res

print(countKeyChanges("aAbBcC"))
print(countKeyChanges("AaAaAaaA"))