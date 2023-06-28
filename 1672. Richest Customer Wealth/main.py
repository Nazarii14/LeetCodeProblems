def maximumWealth(accounts):
    # max_wealth = 0
    # for i in accounts:
    #     if sum(i) > max_wealth:
    #         max_wealth = sum(i)
    # return max_wealth

    return max([sum(i) for i in accounts])

print(maximumWealth([[1,2,3],[3,2,1]]))
print(maximumWealth([[1,5],[7,3],[3,5]]))
