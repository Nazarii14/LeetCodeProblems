def splitWordsBySeparator(words, separator):
    to_return = []
    for i in words:
        while separator + separator in i:
            i = i.replace(separator + separator, separator)
        to_return += i.strip(separator).split(separator)
    return [i for i in to_return if i != '']


print(splitWordsBySeparator(["one.two.three", "four.five", "six"], "."))
print(splitWordsBySeparator(["$easy$", "$problem$"], "$"))
print(splitWordsBySeparator(["|||"], "|"))
print(splitWordsBySeparator(["$$.o.$$."], "$"))
