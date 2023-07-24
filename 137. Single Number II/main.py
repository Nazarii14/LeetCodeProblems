def singleNumber(nums):
    dic = {}
    for i in nums:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1

    for i in dic.keys():
        if dic[i] == 1:
            return i

def singleNumber1(nums):
    not_to_return, to_return = [], []
    for i in nums:
        if i in to_return:
            to_return.remove(i)
            not_to_return.append(i)
        if i not in to_return + not_to_return:
            to_return.append(i)
    return to_return[0]


print(singleNumber1([2,2,3,2]))
print(singleNumber1([0,1,0,1,0,1,99]))