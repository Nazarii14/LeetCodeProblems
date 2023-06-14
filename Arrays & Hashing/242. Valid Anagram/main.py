def isAnagram(s, t):
    if len(s) != len(t):
        return False
    k, g = [], []
    for i in s:
        k.append(i)

    for i in t:
        g.append(i)
    return sorted(k) == sorted(g)

print(isAnagram("anagram", "nagaram"))