def reverseWords(s):
    s = s.strip()
    while '  ' in s:
        s = s.replace('  ', ' ')

    return ' '.join(s.split(' ')[::-1])

print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))
print(reverseWords("a good   example"))
