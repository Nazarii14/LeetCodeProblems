def findWordsContaining(words, x):
    return [i for i in range(len(words)) if words[i].find(x) != -1]

print(findWordsContaining(words = ["leet","code"], x = "e"))
print(findWordsContaining(words = ["abc","bcd","aaaa","cbc"], x = "a"))