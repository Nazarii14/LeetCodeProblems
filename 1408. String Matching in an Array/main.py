def stringMatching(words):
    result = []
    for i in range(len(words)):
        for j in words[:i] + words[i+1:]:
            if words[i] in j and words[i] not in result:
                result.append(words[i])
    return result


print(stringMatching(["mass","as","hero","superhero"]))
print(stringMatching(["leetcode","et","code"]))
print(stringMatching(["blue","green","bu"]))
print(stringMatching(["leetcoder","leetcode","od","hamlet","am"]))
