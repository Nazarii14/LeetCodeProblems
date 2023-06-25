def modifyString(s):
    possible_letters = "abc"
    if s == '?':
        return "a"

    if s[0] == '?':
        s = possible_letters[(possible_letters.find(s[1]) + 1) % 3] + s[1:]

    if s[-1] == '?':
        s = s[:-1] + possible_letters[(possible_letters.find(s[-2]) + 1) % 3]

    for i in range(1, len(s) - 1):
        possible_letters = ['a', 'b', 'c']
        if s[i] == '?':
            if s[i - 1] in possible_letters:
                possible_letters.remove(s[i - 1])
            if s[i + 1] in possible_letters:
                possible_letters.remove(s[i + 1])
            s = s[:i] + possible_letters[0] + s[i + 1:]

    return s


print(modifyString("ubv?w"))
print(modifyString("?zs?"))
print(modifyString("ubva?b"))
print(modifyString("?????????????????????"))
print(modifyString("qwea???bl"))
