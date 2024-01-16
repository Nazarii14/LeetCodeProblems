def accountBalanceAfterPurchase(purchaseAmount):
    k, s = divmod(purchaseAmount, 10)
    if s >= 5:
        k += 1
    return 100 - k * 10


print(accountBalanceAfterPurchase(9))
print(accountBalanceAfterPurchase(15))