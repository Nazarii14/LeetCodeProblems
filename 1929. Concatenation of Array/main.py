def getConcatenation(nums):
    return [i for j in range(2) for i in nums]
    #for j in range(2):
     #   for i in nums:
      #      k.append(i)
    #return k


print(getConcatenation([1,2,1]))
print(getConcatenation([1]))