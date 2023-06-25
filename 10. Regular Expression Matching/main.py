def equal_str(s, p):
    if len(s) != len(p):
        return False

    for i in range(len(s)):
        if s[i] != p[i] and p[i] != ".":
            return False
    return True

def find_str(s, p):
    for i in range(0, len(s) - len(p)+1):
        if equal_str(s[i:i+len(p)], p):
            return i
    return -1

def isMatch(s, p):
    for i in range(1, len(p)):
        if p[i] == "*" and p[i-1].isalpha():
            p = p.replace(p[i-1:i], "*")

    p = p.replace("&", "")

    p = p.replace("**", "*")

    if p.count("*") == 0:
        return equal_str(s, p)

    indeces, splitted = [], p.split("*")

    for i in splitted:
        idx = find_str(s, i)
        indeces.append(idx)
        s = s[idx:]

    return -1 not in indeces


#Test Cases
print(isMatch("abcd", "a*b*c*d"))                #True
print(isMatch("aaa", "ab*"))                     #True
print(isMatch("aaa", "a*"))                      #True
print(isMatch("abdga", "a.*a"))                  #True
print(isMatch("aaafdgfg", "a*af*g"))             #True
print(isMatch("abcddef", "ab*d*"))               #True
print(isMatch("ab", "a.*..."))                   #False
print(isMatch("abddeeeeeedf", "a.dd*d*"))        #True
print(isMatch("sabddeeefegdf", "*a.d*de*f*f"))   #True
print(isMatch("sabdde", "*a.de"))                #False
print(isMatch("aa", "a"))                        #False
print(isMatch("aa", "a"))                        #False
print(isMatch("aab", "c*a*b"))                   #True
print(isMatch("mississippi", "mis*is*p*."))      #True



