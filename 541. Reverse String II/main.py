def reverseStr(s, k):
    a = list(s)
    for i in range(0, len(a), 2 * k):
        a[i:i + k] = reversed(a[i:i + k])
    return "".join(a)


print(reverseStr("abcd", 2))
