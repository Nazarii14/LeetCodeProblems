def noAlpha(s):
    if s == '.' or s.count('.') > 1 or '+' in s or '-' in s: return False
    split = s.split('.')

    for i in split:
        for j in i:
            if j.isalpha():
                return False
    return True if s != '' else False

def isNumber(s):
    signs = ["+-", "-+", "++", "--", '..']
    for i in signs:
        if i in s:
            return False

    if s == '' or s == '.': return False

    while len(s) > 0 and (s[0] == '+' or s[0] == '-'):
        s = s[1:]

    if s == '':
        return False

    s = s.lower()
    split = s.split('e')

    if len(split) == 1: return noAlpha(s)
    if len(split) > 2: return False
    else:
        if '.' in split[1]:
            return False
        if split[0] == '' or split[1] == '':
            return False
        while len(split[1]) > 0 and (split[1][0] == '+' or split[1][0] == '-'):
            split[1] = split[1][1:]
        if noAlpha(split[1]) and noAlpha(split[0]):
            return True

    return False


# True

print(isNumber("32.e-80123"))
print(isNumber("005047e+6"))
print(isNumber("0."))
print(isNumber("2"))
print(isNumber("0089"))
print(isNumber("-0.1"))
print(isNumber("+3.14"))
print(isNumber("4."))
print(isNumber("-.9"))
print(isNumber("2e10"))
print(isNumber("-90E3"))
print(isNumber("3e+7"))
print(isNumber("+6e-1"))
print(isNumber("53.5e93"))
print(isNumber("-123.456e789"))
print()

# False
print(isNumber("abc"))
print(isNumber("1a"))
print(isNumber("1e"))
print(isNumber("e3"))
print(isNumber("99e2.5"))
print(isNumber("--6"))
print(isNumber("-+3"))
print(isNumber("95a54e53"))
print(isNumber("..."))
print(isNumber(".e1"))
print(isNumber(".1."))
print(isNumber("4e+"))
print(isNumber("+"))

