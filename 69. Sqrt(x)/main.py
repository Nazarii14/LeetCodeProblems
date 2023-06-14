def mySqrt(x):
    i = 0
    while True:
        if i * i > x:
            break
        i+=1
    return i - 1

def mySqrt1(x):
    if x == 0: return 0

    l, r = 0, x // 2 + 1
    while l <= r:
        m = l + ((r - l) // 2)
        if m * m < x:
            l = m + 1
        elif m * m > x:
            r = m - 1
        else: return m
    return min(l, r)
print(mySqrt1(2147395599))