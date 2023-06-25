def isPrefixOfWord(sentence, searchWord):
    words = [i if len(i) >= len(searchWord) else '' for i in sentence.split(' ')]
    for i in range(len(words)):
        if words[i] != '' and words[i].find(searchWord) == 0:
            return i+1
    return -1


print(isPrefixOfWord("i love eating burger", "burg"))
print(isPrefixOfWord("this problem is an easy problem", "pro"))
print(isPrefixOfWord("i am tired", "you"))
