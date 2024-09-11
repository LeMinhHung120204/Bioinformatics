def DPChange(money, coins):
    MinNumCoins = [9999999] * (money + 1)
    MinNumCoins[0] = 0

    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                MinNumCoins[m] = min(MinNumCoins[m], MinNumCoins[m - coin] + 1)
    return MinNumCoins[money]


with open('input.inp', 'r') as fi:
    money = int(fi.readline().strip())
    coins = list(map(int, fi.readline().strip().split()))

print(DPChange(money, coins))


