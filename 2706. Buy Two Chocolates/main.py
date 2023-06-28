def buyChoco(prices, money):
    prices = sorted(prices)
    remainder = money - prices[0] - prices[1]
    return money if remainder < 0 else remainder



print(buyChoco([1,2,2], 3))
print(buyChoco([3,2,3], 3))