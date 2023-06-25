def intToRoman(s):
    to_return = 0
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for i in range(len(s) - 1):
        if dic[s[i]] >= dic[s[i + 1]]:
            to_return += dic[s[i]]
        else:
            to_return -= dic[s[i]]

    return to_return + dic[s[-1]]