def maximumNumberOfStringPairs(words):
    counter = 0
    for i in range(len(words)):
        if words[i][::-1] in words[i+1:]:
            counter += 1
    return counter

print(maximumNumberOfStringPairs(["cd", "ac", "dc", "ca", "zz"]))
print(maximumNumberOfStringPairs(["ab", "ba", "cc"]))
