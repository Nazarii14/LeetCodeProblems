def luckyNumbers(matrix):
    result = []
    for i in matrix:
        min_in_i = min(i)
        index_of_min = i.index(min_in_i)
        current_lst = []
        for j in matrix:
            current_lst.append(j[index_of_min])

        if max(current_lst) == min_in_i:
            result.append(min_in_i)
    return result


print(luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
print(luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
print(luckyNumbers([[7,8],[1,2]]))
