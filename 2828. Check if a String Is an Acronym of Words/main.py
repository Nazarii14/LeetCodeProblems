def isAcronym(words, s):
    if len(s) != len(words):
        return False

    for i in range(len(words)):
        if words[i][0] != s[i]:
            return False
    return True


print(isAcronym(words=["alice", "bob", "charlie"], s="abc"))
print(isAcronym(words=["an", "apple"], s="a"))
print(isAcronym(words=["never", "gonna", "give", "up", "on", "you"], s="ngguoy"))
