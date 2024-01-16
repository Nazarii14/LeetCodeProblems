def isMatch(s, p):
    cache = {}

    def dfs(i, j):
        if (i, j) in cache:
            return cache[(i, j)]
        if i >= len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False

        match = i < len(s) and (s[i] == p[j] or p[j] == '.')

        if (j + 1) < len(p) and p[j + 1] == '*':
            cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
            return cache[(i, j)]

        if match:
            cache[(i, j)] = dfs(i + 1, j + 1)
            return cache[(i, j)]
        cache[(i, j)] = False
        return False

    return dfs(0, 0)



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



