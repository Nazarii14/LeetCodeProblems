def lengthOfLastWord(s):
    if len(s) == 0:
        return 0
    length = 0
    for i in range(len(s)-1):
        if s[i] == ' ' and s[i+1] != ' ':
            length = 0
        elif not s[i] == ' ':
            length += 1
    return length + 1 if s[-1] != ' ' else length

print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord(""))
print(lengthOfLastWord("   fly me   to   the moo"))