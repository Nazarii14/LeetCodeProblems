def isValid(s):
    result = [s[0]]
    opened_p = ["(", "[", "{"]
    closed_p = [")", "]", "}"]

    for i in s[1:]:
        if i in closed_p:
            if len(result) == 0:
                return False
            elif result[-1] == opened_p[closed_p.index(i)]:
                result.pop()
            else:
                return False
        else:
            result.append(i)
    return len(result) == 0


print(isValid("(){}}{"))

